
from utils.retriever import retrieve_docs
from utils.reranker import rerank
from utils.context_builder import build_context
from utils.cache import get_cache, set_cache
from utils.llm import call_llm

def generate_response(query):
    cached = get_cache(query)
    if cached:
        return cached

    docs = retrieve_docs(query)
    ranked_docs = rerank(query, docs)
    context = build_context(ranked_docs)

    response = call_llm(query, context)
    set_cache(query, response)
    return response
