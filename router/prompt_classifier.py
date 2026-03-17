import ollama

def decider(prompt):
    response = ollama.chat(model="mistral",messages=[{
        "role": "user",
        "content":
        f"""
            Você é um classificador de prompts.

            Sua tarefa é classificar a entrada do usuário em exatamente uma das seguintes categorias:

            - code → programação, scripts, debugging, tarefas técnicas de código
            - general → perguntas gerais ou conversa casual
            - explanation → explicações detalhadas, conceitos ou "como funciona"
            - analysis → raciocínio, comparação ou análise mais profunda
            - short_query → perguntas muito curtas ou simples

            Regras:
            - Retorne APENAS o nome da categoria
            - Não explique sua resposta
            - Não retorne nada além da categoria
            - A resposta deve ser em letras minúsculas

            Prompt do usuário:
            "{prompt}"

        """,
    }
    ])
    resultado = response.message.content
    return resultado