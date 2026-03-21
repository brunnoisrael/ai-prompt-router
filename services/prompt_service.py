from router.prompt_classifier import decider
from router.model_router import gateway
from llm.ollama_client import OllamaClient

"""
    1. Efetua a chamada (prompt_classifier.py) da SLM para definir qual categoria o prompt do usuario se enquadra
    2. Efetua a chamada (model_router.py) para chamar a LLM da categoria definida para responder o prompt.
    
"""

def workload(prompt):
    classified_prompt = decider(prompt)
    result_workload = gateway(classified_prompt)
    response_llm = OllamaClient.ollama_llm(result_workload)
    return response_llm