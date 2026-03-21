class ModelRegistry:
    def __init__(self):
        self.models = {
            "codellama": {
                "capabilities": ["code", "debug"]
            },
            "llama3": {
                "capabilities": ["geral", "explicação"]
            },
            "mistral": {
                "capabilities": ["análises", "explicação"]
            },
            "phi3": {
                "capabilities": ["pergunta_curta", "rápido"]
            }
        }
    def models_for_capabilities(self, capability:str):
        return [
            model_name
            for model_name, data in self.models.items()
            if capability in data ["capabilities"]
        ]
    
    def get_default_model(self):
        return "mistral"
