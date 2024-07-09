## Descrição

Um projeto voltado para educação, fornecendo funcionalidades além de feedback, com base no modelo GPT.

## Estrutura do Projeto

```
.
├── api
│   ├── controllers
│   │   ├── feedback_controller.py
│   │   ├── mind_map_controller.py
│   │   ├── study_guide_controller.py
│   │   └── exercises_controller.py
│   ├── models
│   │   ├── prompts
│   │   │   ├── feedback_prompt.py
│   │   │   ├── mind_map_prompt.py
│   │   │   ├── study_guide_prompt.py
│   │   │   └── exercises_prompt.py
│   │   ├── request
│   │   │   ├── feedback_request.py
│   │   │   ├── mind_map_request.py
│   │   │   ├── study_guide_request.py
│   │   │   └── exercises_request.py
│   │   └── response
│   │       └── feedback_response.py
│   ├── routes
│   │   ├── feedback_routes.py
│   │   ├── mind_map_routes.py
│   │   ├── study_guide_routes.py
│   │   └── exercises_routes.py
│   └── services
│       ├── gpt_services.py
│       ├── feedback_service.py
│       ├── mind_map_service.py
│       ├── study_guide_service.py
│       └── exercises_service.py
├── .env
├── main.py
├── README.md
└── requirements.txt

```

## Estrutura de Diretórios

- **api/controllers/**: Controladores que recebem as requisições HTTP, chamam os serviços correspondentes e retornam as respostas.
- **api/models/prompts/**: Prompts para interação com o modelo GPT da OpenAI.
- **api/models/request/**: Modelos de requisição para estruturar os dados recebidos nas requisições HTTP.
- **api/models/response/**: Modelos de resposta para estruturar os dados retornados pelos serviços.
- **api/routes/**: Definição das rotas da API FastAPI para cada funcionalidade.
- **api/services/**: Lógica de negócio dos serviços que interagem com a API da OpenAI e processam os dados.


## Pré-requisitos

1. Configure Chave da API OpenAI

Antes de começar, certifique-se de criar um arquivo `.env` com a variável `OPENAI_API_KEY` contendo a chave da API do OpenAI. Esta chave permite que a aplicação se autentique e faça solicitações aos modelos de inteligência artificial da OpenAI

Exemplo:

```bash
OPENAI_API_KEY=your_openai_api_key
```
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Rotas


<details>
  <summary>Gerar Feedback</summary>&nbsp;

   
   - Endpoint:

```bash
/feedback/generate/
```
   - Método:
```bash
POST
```

- Request:

```json
{
  "question": {
    "title": "string",
    "question_id": "string",
    "response": {
      "answer": "string",
      "response_id": "string"
    }
  },
  "feedbackList": [
    "string"
  ]
}

```


- Response:

```json
{
    "title": "{título da pergunta}",
    "question_id": "{id da pergunta}",
    "response": {
        "answer": "{resposta do aluno à pergunta}",
        "response_id": "{id da resposta}",
        "feedback": "{feedback gerado por você sobre a resposta do aluno}",
        "type": "{tipo da resposta, sendo: acerto, acerto parcial ou erro}",
        "wrong_snippets": ["{trechos da resposta marcadas como errada}"]
    }
}

```

 </details>

## Documentação Swagger:
Você pode visualizar a documentação Swagger interativa para explorar os detalhes e testar o endpoint em 


http://127.0.0.1:8000/docs

Lembre-se de que, para acessar a documentação Swagger, o servidor FastAPI precisa estar em execução localmente.
