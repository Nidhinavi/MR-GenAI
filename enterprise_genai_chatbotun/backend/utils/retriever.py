
from sentence_transformers import SentenceTransformer
import faiss, numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
docs = ["discount on mobiles", "fashion sale", "customer segmentation marketing"]

emb = model.encode(docs)
index = faiss.IndexFlatL2(len(emb[0]))
index.add(np.array(emb))

def retrieve_docs(query):
    q = model.encode([query])
    D,I = index.search(np.array(q), k=3)
    return [docs[i] for i in I[0]]
