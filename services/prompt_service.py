import time
from router.prompt_classifier import decider
from router.model_router import gateway
from llm.ollama_client import OllamaClient
from observability.metrics import Count_requests, Response_time, Errors_requests

"""
    1. Efetua a chamada (prompt_classifier.py) da SLM para definir qual categoria o prompt do usuario se enquadra
    2. Efetua a chamada (model_router.py) para chamar a LLM da categoria definida para responder o prompt.
    
"""

def workload(prompt):

    classified_prompt = decider(prompt)
    result_workload = gateway(classified_prompt)
    client = OllamaClient()

    # Horário de inicio da requisição
    start_time = time.time()

    try:
        response_llm = client.ollama_llm(model=result_workload, prompt=prompt)

        Count_requests.labels(model=result_workload).inc()

        return response_llm
    
    except:

        Errors_requests.labels(model=result_workload).inc()
        raise

    finally:
        
        # Duração da requisição
        duration = time.time() - start_time
        Response_time.labels(model=result_workload).observe(duration)

    