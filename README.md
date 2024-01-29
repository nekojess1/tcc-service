## Descrição

Um projeto voltado para educação, fornecendo funcionalidades além de feedback, com base no modelo GPT.

## Estrutura do Projeto

.
├── api
│ ├── models
│ │ ├── context
│ │ │ └── feedback_prompt.py
│ │ ├── request
│ │ │ └── feedback_request.py
│ │ └── response
│ │ └── feedback_response.py
│ ├── routes
│ │ └── generate_feedback.py
│ └── services
│ └── generate_feedback.py
├── .env
├── main.py
├── README.md
└── requirements.txt

## Pré-requisitos

Antes de começar, certifique-se de criar um arquivo `.env` com a variável `OPENAI_API_KEY` contendo a chave da API do OpenAI.

Exemplo:

```bash
OPENAI_API_KEY=your_openai_api_key
```

## Configuração do Ambiente

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Rotas

- Gerar Feedback 

    Endpoint:
    ```bash
    /generate-feedback/
    ```
    Método:
    ```bash
    POST
    ```

        

    Corpo da Requisição (JSON):

    ```json
    {
        "title": "Título da Pergunta",
        "question_id": "ID da Pergunta",
        "response": {
            "answer": "Resposta do Aluno à Pergunta",
            "email": "Email do Aluno",
            "response_id": "ID da Resposta",
            "form_id": "ID do Formulário"
        }
    }
    ```
## Documentação Swagger:
Você pode visualizar a documentação Swagger interativa para explorar os detalhes e testar o endpoint em 


http://127.0.0.1:8000/docs

Lembre-se de que, para acessar a documentação Swagger, o servidor FastAPI precisa estar em execução localmente.
