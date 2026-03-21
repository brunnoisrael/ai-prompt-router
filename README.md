# 🚀 AI Prompt Router

Um projeto simples de **roteamento inteligente de prompts usando múltiplos modelos LLM**, com arquitetura inspirada em plataformas reais de IA.

---

## 🧠 Ideia

O sistema recebe um prompt, classifica o tipo da requisição e escolhe automaticamente o melhor modelo para responder.

```text
Client → API → Classifier → Router → Model Registry → LLM → Response
```

---

## ⚙️ Tecnologias

* Python
* Flask
* Ollama
* Docker (opcional)
* python-dotenv

---

## 📦 Estrutura do Projeto

```
ai-prompt-router/

app/
│
├── api/
│   └── routes.py              # Camada HTTP (entrada da API)
│
├── services/
│   └── prompt_service.py      # Orquestra o fluxo completo
│
├── router/
│   ├── prompt_classifier.py   # Classifica o prompt
│   └── model_router.py        # Decide qual modelo usar
│
├── llm/
│   ├── ollama_client.py       # Integração com Ollama
│   └── model_registry.py      # Catálogo de modelos e capabilities
│
└── main.py                    # Inicialização da aplicação

docker/
│
├── Dockerfile
├── docker-compose.yml
└── prometheus.yml

requirements.txt
README.md
```

---

## 🔥 Fluxo de Execução

1. O cliente envia um prompt para `/prompt`
2. A API recebe a requisição
3. O `prompt_service` orquestra o fluxo:

   * Classifica o prompt
   * Decide o modelo ideal
   * Executa via client
4. O sistema retorna a resposta

---

## 🧠 Classificação de Prompts

Categorias suportadas:

* `code`
* `general`
* `explanation`
* `analysis`
* `short_query`

---

## 🧩 Model Capabilities

Os modelos são definidos com base em suas capacidades:

| Modelo    | Capabilities          |
| --------- | --------------------- |
| codellama | code, debug           |
| llama3    | general, explanation  |
| mistral   | analysis, explanation |
| phi3      | short_query, fast     |

---

## 🔐 Autenticação

A API usa autenticação simples via header:

```
Authorization: Bearer <API_TOKEN>
```

---

## ▶️ Como rodar o projeto

### 1. Clonar repositório

```
git clone <repo-url>
cd ai-prompt-router
```

---

### 2. Criar ambiente virtual

```
python -m venv venv
venv\Scripts\activate  # Windows
```

---

### 3. Instalar dependências

```
pip install -r requirements.txt
```

---

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env`:

```
SECRET_KEY=seu_token_aqui
OLLAMA_URL=http://localhost:11434
```

---

### 5. Rodar aplicação

```
python app/main.py
```

---

## 🧪 Exemplo de requisição

```
POST /prompt
```

Body:

```json
{
  "prompt": "explique como funciona o kubernetes"
}
```

Header:

```
Authorization: Bearer seu_token_aqui
```

---

## 🐳 Rodando com Docker (opcional)

```
docker-compose up --build
```

---

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo demonstrar:

* Arquitetura de sistemas com LLMs
* Separação de responsabilidades
* Roteamento inteligente de modelos
* Integração com provedores de IA

---

## 🚀 Possíveis melhorias

* Fallback automático entre modelos
* Métricas e logs
* Cache de respostas
* Rate limiting por API key
* Suporte a múltiplos provedores de LLM

---

## 📌 Observações

* O projeto é um MVP educacional
* Não utiliza autenticação completa (ex: OAuth, JWT)
* Pode ser facilmente estendido para ambientes produtivos

---

## 👨‍💻 Autor

Projeto desenvolvido para estudo de arquitetura de IA e sistemas distribuídos.
