from prometheus_client import Counter, Histogram

Count_requests = Counter("llm_requests_count", "Quantidade de requisições enviadas para o modelo", ["model"])

Response_time = Histogram("llm_response_time", "Tempo de resposta pelo modelo", ["model"])

Errors_requests = Counter("llm_requests_erros", "Quantidade de erros de requisições", ["model"])