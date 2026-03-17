from router.prompt_classifier import decider
from router.model_router import gateway

def workload(prompt):
    classified_prompt = decider(prompt)
    resultado_workload = gateway(classified_prompt)
    return resultado_workload