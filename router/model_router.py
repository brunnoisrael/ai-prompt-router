from llm.model_registry import ModelRegistry

def gateway(classified_prompt):
        
    registry = ModelRegistry()
    models = registry.models_for_capabilities(classified_prompt)

    if models:
        model = models[0]
    else:
        model = registry.get_default_model()
    
    return model