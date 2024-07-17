## Descrição

Este projeto utiliza a inteligência artificial generativa, em especial o modelo GPT da OpenAI, para apoiar educadores. Ele oferece funcionalidades como correção de respostas com feedback, geração de mapas mentais, guias de estudo e exercícios personalizados, melhorando a experiência de aprendizado e auxiliando o trabalho dos educadores.

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
│   │   │   ├── exercises
│   │   │   │   ├── exercises_prompt.py
│   │   │   │   ├── exercises_examples.py
│   │   │   │   └── exercises_instructions.txt
│   │   │   ├── mind_maps
│   │   │   │   ├── mind_map_prompt.py
│   │   │   │   ├── mind_map_examples.py
│   │   │   │   └── mind_map_instructions.txt
│   │   │   ├── study_guides
│   │   │   │   ├── study_guide_prompt.py
│   │   │   │   ├── study_guide_examples.json
│   │   │   │   └── study_guide_instructions.txt
│   │   │   └── feedbacks
│   │   │       ├── feedback_prompt.py
│   │   │       ├── feedback_examples.py
│   │   │       └── feedback_instructions.txt
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

Para realizar esse passo é necessário ter python instalado. A versão utilizada foi a 3.12.4.

```bash
pip install -r requirements.txt
```

3. Como executar:

Para executar o projeto, utilize o seguinte comando no terminal:

```bash
python -m uvicorn main:app --reload
```

## Endpoints


<details>
  <summary>Gerar Feedback</summary>&nbsp;

   Este endpoint permite gerar feedback personalizado com base na resposta do aluno. A resposta é processada utilizando o modelo GPT da OpenAI para fornecer feedback construtivo.
   
   - Rota:

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

 <details>
  <summary>Gerar Mapa Mental</summary>&nbsp;
   
Este endpoint gera um mapa mental com base no conteúdo fornecido na requisição.
   
   - Rota:

```bash
/mind-map/generate/
```
   - Método:
```bash
POST
```

- Request:

```json
{
  "subject": "string",
  "language": "string"
}

```


- Response:

```json

  {
    "nodes": [
      { "id": "string", "description": "string" }
    ],
    "edges": [
      { "from_node": "string", "to_node": "string"}
    ]
  }
      

```

 </details>

  <details>
  <summary>Gerar Guia de Estudo</summary>&nbsp;
   
Este endpoint gera um guia de estudo estruturado com base nos tópicos fornecidos na requisição, quantidade de dias, dias da semana e horas por dia.
   
   - Rota:

```bash
/study-guide/generate/
```
   - Método:
```bash
POST
```

- Request:

```json

{
  "daysDuration": 0,
  "daysOfWeek": [
    "string"
  ],
  "hoursPerDay": "string",
  "topics": [
    "string"
  ],
  "language": "string"
}

```


- Response:

```json

{
    "guide": [
        {
            "day": "{study day number}",
            "dayOfWeek": "{day of the week, like Monday}",
            "contents": [
                {
                    "studySubject": {
                        "subject": "{subject of study}",
                        "topic": "{topics of the subject}",
                        "description": "{description of what should be studied, including main points}",
                        "supportingMaterials": ["list of recommended materials, such as books, films, etc."],
                        "hoursOfStudy": "{study hours for this topic}"
                    }
                }
            ]
        }
    ]
}
      

```

 </details>

 
  <details>
  <summary>Gerar Exercícios</summary>&nbsp;
   
Este endpoint gera exercícios com base na lista de assuntos recebida. Pode se definir a quantidade de questões, a dificuldade, se é múltipla escolha ou não e a quantidade de alternativas. 
   
   - Rota:

```bash
/study-guide/generate/
```
   - Método:
```bash
POST
```

- Request:

```json

{
  "topics": [
    {
      "name": "string",
      "number_of_questions": 0,
      "difficulty": "string",
      "multiple_choice_qty": 0,
      "multiple_choice_options": 0,
      "open_ended_qty": 0
    }
  ],
  "questions_example": [
    "string"
  ]
}

```


- Response:

```json

{
  "exercises": [
    {
      "topic": "Topic Name Here",
      "questions": [
        {
          "type": "multiple_choice",
          "question": "Insert multiple-choice question here.",
          "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
          "answer": "Insert correct answer here"
        },
        {
          "type": "open_ended",
          "question": "Insert open-ended question here.",
          "answer": "Insert correct answer here"
        }
      ]
    },
    {
      "topic": "Another Topic Name Here",
      "questions": [
        {
          "type": "multiple_choice",
          "question": "Insert multiple-choice question here.",
          "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
          "answer": "Insert correct answer here"
        },
        {
          "type": "open_ended",
          "question": "Insert open-ended question here.",
          "hints": ["Insert hint(s) to solve the question, if necessary."],
          "answer": "Insert correct answer here"
        }
      ]
    }
  ]
}

      

```

 </details>

## Documentação Swagger:
Você pode visualizar a documentação Swagger interativa para explorar os detalhes e testar o endpoint em 


http://127.0.0.1:8000/docs

Lembre-se de que, para acessar a documentação Swagger, o servidor FastAPI precisa estar em execução localmente.


