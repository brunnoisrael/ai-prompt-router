import requests
import os

OLLAMA_URL = os.getenv("OLLAMA_URL")

class OllamaClient:
    def ollama_llm(self, model, prompt):
        response = requests.post(f"{OLLAMA_URL}/api/generate", json={
            "model": model,
            "prompt": prompt,
            "stream": False
        },
        timeout=150)

        response.raise_for_status()
        data = response.json()

        return {
            "model": model,
            "response": data.get("response", ""),
            "status": "success"
        }