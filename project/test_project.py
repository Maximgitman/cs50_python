from project import read_glove_embeddings, change_index
import torch


def test_embeddings_knrm():
    assert len(torch.load("./static/embeddings_knrm.bin")["weight"]) != 0
    assert len(torch.load("./static/embeddings_knrm.bin")["weight"]) == 87164

def test_glove_embeddings():
    assert type(read_glove_embeddings("./static/glove.6B.50d.txt")) == dict
    assert len(read_glove_embeddings("./static/glove.6B.50d.txt")) == 38509

def test_create_index():
    assert change_index(0) == False
    assert change_index(1) == True
