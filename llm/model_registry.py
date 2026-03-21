class ModelRegistry:
    def __init__(self):
        self.models = {
            "codellama": {
                "capabilities": ["code", "debug"]
            },
            "llama3": {
                "capabilities": ["general", "explanation"]
            },
            "mistral": {
                "capabilities": ["analysis", "explanation"]
            },
            "phi3": {
                "capabilities": ["short_query", "fast"]
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
