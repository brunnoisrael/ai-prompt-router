from router.prompt_classifier import decider
from router.model_router import gateway

"""
    1. Efetua a chamada (prompt_classifier.py) da SLM para definir qual categoria o prompt do usuario se enquadra
    2. Efetua a chamada (model_router.py) para chamar a LLM da categoria definida para responder o prompt.
    
"""

def workload(prompt):
    classified_prompt = decider(prompt)
    resultado_workload = gateway(classified_prompt)
    return resultado_workload