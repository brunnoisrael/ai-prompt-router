import ollama

def gateway(classified_prompt):
    classified_prompt = classified_prompt.strip()
    modelo = ""
    if classified_prompt == "code":
        modelo = "mistral"
    if classified_prompt == "genaral":
        modelo = "gpt"
    response = ollama.chat(model=modelo,messages=[{
        "role": "user",
        "content": f"""
        RESPONDA EM PORTUGUES CASO NAO DETECTE IDIOMA EXPLICITO

        {classified_prompt}

        """,
    }
    ])
    resultado = response.message.content
    return resultado