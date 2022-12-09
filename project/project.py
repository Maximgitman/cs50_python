from flask import Flask, jsonify, request, render_template
import torch.nn.functional as F
from typing import Dict, List
from langdetect import detect
import numpy as np
import string
import faiss
import torch
import nltk
import json
import os


class GaussianKernel(torch.nn.Module):
    def __init__(self, mu: float = 1., sigma: float = 1.):
        super().__init__()
        self.mu = mu
        self.sigma = sigma

    def forward(self, x):
        norm_squared = (x - self.mu)**2
        k = torch.exp(-norm_squared/(2*self.sigma**2))
        return k


class KNRM(torch.nn.Module):
    def __init__(self, embedding_matrix: torch.FloatTensor, freeze_embeddings: bool = True, 
                kernel_num: int = 13, sigma: float = 0.1, exact_sigma: float = 0.001,
                out_layers: List[int] = []):
        super().__init__()
        self.embeddings = torch.nn.Embedding.from_pretrained(
            embedding_matrix,
            freeze=freeze_embeddings,
            padding_idx=0
        )

        self.kernel_num = kernel_num
        self.sigma = sigma
        self.exact_sigma = exact_sigma
        self.out_layers = out_layers

        self.kernels = self._get_kernels_layers()
        self.mlp = self._get_mlp()
        self.out_activation = torch.nn.Sigmoid()

    def _get_kernels_layers(self) -> torch.nn.ModuleList:
        l = np.linspace(start=-1, stop=0, endpoint=True, num=self.kernel_num)[1::2]
        r = np.linspace(start=0, stop=1, endpoint=True, num=self.kernel_num)[1::2]
        mus = np.hstack((l, r, 1.))
        
        # For las value sigma = exact sigma
        kernels = torch.nn.ModuleList()
        for mu in range(mus.shape[0]):
            if mu == (mus.shape[0]-1):
                k = GaussianKernel(mu=mus[mu], sigma=self.exact_sigma)
            else:
                k = GaussianKernel(mu=mus[mu], sigma=self.sigma)
            kernels.add_module(f"kernels_{mu}", k)

        return kernels

    def _get_mlp(self) -> torch.nn.Sequential:
        model_seq = torch.nn.Sequential()
        if len(self.out_layers) == 0:
            l1 = torch.nn.Linear(self.kernel_num, 1)
            model_seq.add_module(f"final_layer{0}", l1)
        else:
            in_f = self.kernel_num
            for ol in self.out_layers:
                l1 = torch.nn.Linear(in_f, ol)
                r1 = torch.nn.ReLU()
                model_seq.add_module(f"layer_{ol}",l1)
                model_seq.add_module(f"activation_{ol}",r1)
                in_f = ol
            model_seq.add_module(f"final_layer_{ol}", torch.nn.Linear(in_f, 1))

        return model_seq


    def forward(self, input_1: Dict[str, torch.Tensor], input_2: Dict[str, torch.Tensor]) -> torch.FloatTensor:
        logits_1 = self.predict(input_1)
        logits_2 = self.predict(input_2)

        logits_diff = logits_1 - logits_2

        out = self.out_activation(logits_diff)
        return out

    def _get_matching_matrix(self, query: torch.Tensor, doc: torch.Tensor) -> torch.FloatTensor:

        query_embedding = self.embeddings(query)
        doc_embedding = self.embeddings(doc)
        
        distance = F.cosine_similarity(query_embedding[..., :, None, :], doc_embedding[..., None, :, :], dim=-1)
        
        return distance

    def _apply_kernels(self, matching_matrix: torch.FloatTensor) -> torch.FloatTensor:
        KM = []
        for kernel in self.kernels:
            # shape = [B]
            K = torch.log1p(kernel(matching_matrix).sum(dim=-1)).sum(dim=-1)
            KM.append(K)

        # shape = [B, K]
        kernels_out = torch.stack(KM, dim=1)
        return kernels_out

    def predict(self, inputs: Dict[str, torch.Tensor]) -> torch.FloatTensor:
        # shape = [Batch, Left], [Batch, Right]
        query, doc = inputs['query'], inputs['document']
        # shape = [Batch, Left, Right]
        matching_matrix = self._get_matching_matrix(query, doc)
        # shape = [Batch, Kernels]
        kernels_out = self._apply_kernels(matching_matrix)
        # shape = [Batch]
        out = self.mlp(kernels_out)
        return out


def hadle_punctuation(inp_str: str) -> str:
    for symb in string.punctuation:
        inp_str = inp_str.replace(symb, " ")
    return inp_str


def simple_preproc(inp_str: str) -> List[str]:
    cleaned = hadle_punctuation(inp_str).lower()
    tokens = nltk.word_tokenize(cleaned)
    return tokens


def get_embeddings_docs(documents):
    embeded_docs = []    
    for doc in documents:
        tokens = simple_preproc(doc)
        emb_token = np.array([glove_embeddings[token] for token in tokens if glove_embeddings.get(token) is not None])

        if emb_token.shape[0] == 0:
            embeded_docs.append(np.zeros((50)))
        else:
            embeded_docs.append(np.mean(emb_token, axis=0))

    embeded_docs = np.array(embeded_docs)
    return embeded_docs


def query_emb_and_idx(documents):
    embeded_docs = []   
    docs_ids_tokens = []
    max_len = -1 
    for doc in documents:
        tokens = simple_preproc(doc)
        emb_token = np.array([glove_embeddings[token] for token in tokens if glove_embeddings.get(token) is not None])
        doc_tokens = list(map(lambda token: vocab.get(token, vocab["OOV"]), tokens))
        max_len = max(len(doc_tokens), max_len)
        docs_ids_tokens.append(doc_tokens)

        if emb_token.shape[0] == 0:
            embeded_docs.append(np.zeros((50)))
        else:
            embeded_docs.append(np.mean(emb_token, axis=0))
    
    padded_batch = []
    for id in docs_ids_tokens:
        pad_len = max_len - len(id)
        padded_batch.append(id + [0] * pad_len)
        
    padded_batch = torch.LongTensor(padded_batch)
    embeded_docs = np.array(embeded_docs)
    
    return embeded_docs, padded_batch


def get_embeddings_docs_vocab(ids_similar):
    docs_ids_tokens = []
    max_len = -1
    for ids in ids_similar:
        doc = doc_text[ids]
        doc_tokens = simple_preproc(doc)
        doc_tokens = list(map(lambda token: vocab.get(token, vocab["OOV"]), doc_tokens))
        max_len = max(len(doc_tokens), max_len)
        docs_ids_tokens.append(doc_tokens)

    padded_batch = []
    for id in docs_ids_tokens:
        pad_len = max_len - len(id)
        padded_batch.append(id + [0] * pad_len)
    padded_batch = torch.LongTensor(padded_batch)
    
    return padded_batch


def read_glove_embeddings(file_path: str) -> Dict[str, List[str]]:
    embeddings_dict = {}
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.array(values[1:], "float32")
            embeddings_dict[word] = vector
    return embeddings_dict


app = Flask(__name__)

EMB_PATH_KNRM = "./static/embeddings_knrm.bin"
MLP_PATH = "./static/knrm_mlp.bin"
EMB_PATH_GLOVE = "./static/glove.6B.50d.txt"
VOCAB_PATH = "./static/vocab.json"

embeddings_knrm = torch.load(EMB_PATH_KNRM)["weight"]
model = KNRM(embedding_matrix=embeddings_knrm)
model.mlp.load_state_dict(torch.load(MLP_PATH))
glove_embeddings = read_glove_embeddings(EMB_PATH_GLOVE)


def main():
    embeddings_knrm = torch.load("./static/embeddings_knrm.bin")["weight"]
    glove_embeddings = read_glove_embeddings("./static/glove.6B.50d.txt")
    index_created = change_index(0)

def change_index(action_num: int):
    if action_num == 0:
        return False
    else:
        return 1

with open(VOCAB_PATH) as json_file:
    vocab = json.load(json_file)

index_created = False


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/query", methods=["POST"])
def query():
    if request.method == "POST":
        if index_created:
            k = 100
            sugestions = {"lang_check" : [], "suggestions" : []}
            queries = json.loads(request.json)["queries"]
            emb_queries_glove, indexes_queries_vocab  = query_emb_and_idx(queries)
            top_k = 10
            
            for query in range(len(queries)):
                if detect(queries[query]) == "en":
                    lang_check = True

                    D, I = index.search(emb_queries_glove[query].reshape(1, -1).astype(np.float32), k)                   
                    
                    docs_filter = get_embeddings_docs_vocab(I[0])
                    quer_repeat = indexes_queries_vocab[query].repeat(docs_filter.shape[0], 1)
    
                    input = {"query" : quer_repeat, 
                            "document" : docs_filter}

                    with torch.no_grad():
                        model.eval()
                        preds = model.predict(input)
                        preds_np = preds.detach().numpy().reshape(-1)
                        indices = np.argsort(preds_np)[::-1][:top_k]

                    suggestions = [(doc_keys[i], doc_text[i]) for i in I[0][indices]]
                    sugestions["lang_check"].append(lang_check)
                    sugestions["suggestions"].append(suggestions)
                else:
                    lang_check = False
                    sugestions["lang_check"].append(lang_check)
                    sugestions["suggestions"].append(None)
            return jsonify(sugestions)
        else:
            return jsonify({"status" : "FAISS is not initialized!"})


@app.route("/update_index", methods=["POST"])
def update_index():
    if request.method == "POST":
        print("update_index")
        global index, doc_keys, doc_text, index_created, t_matrix
        
        documents = json.loads(request.json)["documents"]
        doc_keys = []
        doc_text = []

        for k, v in documents.items():
            doc_keys.append(k)
            doc_text.append(v)

        t_matrix = get_embeddings_docs(doc_text)    # (100577, 50)
        index = faiss.IndexFlatL2(t_matrix.shape[1])

        index.add(t_matrix.astype(np.float32))

        index_created = True
        print("update_index_done")
        return jsonify({"status" : "ok", "index_size" : index.ntotal}) 


if __name__=="__main__":
    main()
    app.run()