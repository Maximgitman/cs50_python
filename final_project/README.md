# Quora questions similarity
#### Video Demo:  <URL HERE> 
#### Description:

As a project finale, a system of prompts for similar questions based on Quora site data was implemented. Search exclusively on the main issue (title) without specifying the details (additional description).

The system is represented by a microservice based on Flask. The top-level pipeline and evaluation can be represented as follows:

Requests are filtered by language (using the LangDetect library) - all requests for which a specific language does not match "en" are detected. Then there is a search for candidate questions using FAISS (by coincidence of vectors) - in this part, the vectorization of those words is partially eliminated, embeddings are only in the original GLOVE vectors. These candidates are re-ranked by the KNRM model, after which up to 10 candidates are issued as a response.

EMB_PATH_KNRM — KNRM embeddings matrix obtained as part of model training (torch.save(Solution(...).model.embeddings.state_dict())). The order of the tokens is according to the specified VOCAB_PATH JSON dictionary. In this key, this is a word, the value is an index in the embedding matrix. The MLP part is in the MLP_PATH environment. Raw GLOVE embeddings (for example, for vectorization when searching for neighbors - to find out which excitation vectors were random, but were obtained earlier) in EMB_PATH_GLOVE.

The service can be started with the command FLASK_APP=app.py flask run --port 11000

Next, you need to implement two handles: for leaving (for searching for similar questions) and for creating a FAISS index.

/query - accepts a POST request. Should return json where status='FAISS not initialized!' in case no questions were loaded in the solution to search using the second method.

Request format for request:

json request, searching for the 'queries' key, the value of which is a list of strings with questions (Dict[str, List[str]]).

The response format (in the case of a created index) is json with two fields. lang_check described whether the request was recognized as English (List[bool], True/False values), sentences were recognized as List[Optional[List[Tuple[str, str]]]].

In this list, for each request from the request questions, you must specify a list (up to 10) of found cases, where each question is represented as a Tuple, in which the first value is the text id (see below), the second is the raw text of a similar request itself. If the language check failed (not English), there was some kind of processing failure - not in the list instead of the answer ([[(..., or ...), (..., ...) , .. .], Nobody, ... ]).

/update_index - a POST request is taken, in which documents are often found in json, Dict[str,str] - all documents, where the key is the id of the text, the value is the text itself. 200 seconds are given for preprocessing and index creation. The returned json should have two keys: status (well, if everything goes smoothly) and index_size, the value of which is a single integer that stores the number of documents in the index.

