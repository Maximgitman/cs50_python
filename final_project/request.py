import json
import requests
import time

start = time.time()
with open("documents.json", "r") as f:
    documents = json.load(f)

with open("queries.json", "r") as f:
    queries = json.load(f)

req = requests.get("http://127.0.0.1:5000")

req = requests.post("http://127.0.0.1:5000/update_index", json=json.dumps(documents))
print(req.json())
q = time.time()
req = requests.post("http://127.0.0.1:5000/query", json=json.dumps(queries))
print(json.dumps(queries, indent=4))
print(json.dumps(req.json(), indent=4))
print(time.time() - q)
print(round(time.time() - start))
