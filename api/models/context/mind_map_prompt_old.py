input_example = """
    {
      "questions": [
        {
          "title": "{Question title}",
          "question_id": "{Question ID}",
          "responses": [
            {
              "answer": "{Question Response}",
              "response_id": "{Response ID}",
              "feedback": "{Question Feedback}",
              "email": "{Student email}",
              "form_id": "{Form ID}",
              "type": "{Question Type}"
            }
          ]
        }
      ]
    }
    """
    
output_example = """
{
  "nodes": [
    { "id": "0", "description": "<{Mind Map Subject}>" },
    { "id": "1", "description": "<{Subtopic 1}>" },
    { "id": "2", "description": "<{Subtopic 2}>" },
    { "id": "3", "description": "<{Subtopic 3}>" }
  ],
  "edges": [
    { "from_node": "0", "to_node": "1"},
    { "from_node": "1", "to_node": "2"},
    { "from_node": "1", "to_node": "3"},
    { "from_node": "0", "to_node": "2"},
    { "from_node": "2", "to_node": "3"}
  ]
}
"""

rules = """
    1 - Você receberá uma lista de perguntas com as respostas dos alunos.
    2 - Foque nas respostas marcadas com "type" como "ERRO" ou "ACERTO_PARCIAL".
    3 - Pesquise sobre os temas das respostas incorretas e colete as principais informações.
    4 - Nunca utilize as respostas dos alunos como conteúdo para o mapa mental.
    5 - Certifique-se da credibilidade do texto antes de incluí-lo no mapa.
    6 - Crie conexões entre assuntos relacionados.
    7 - Adicione tópicos marcando o assunto, como: causa, consequência, origem, desfecho.
    8 - Ao criar a descrição, caso seja extensa, use <BR/> para quebrar e facilitar a visualização.
    9 - Envolve o texto da descrição com tags HTML, como "<Subtópico 1<BR/>com mais texto>".
    10 - O primeiro nó deve ser o tema central, ou "Conceitos Gerais" se os temas forem diferentes.
    11 - Um grafo sempre deve ter pelo menos uma aresta.
    12 - Verifique todas as possíveis relações entre os tópicos e adicione edges entre tópicos relacionados.
    13 - Crie sub-nós que explicitem detalhes ou consequências dos tópicos principais.
    14 - Explore ao máximo as ligações entre os temas e subtemas, permitindo múltiplos níveis de profundidade conforme necessário.
    15 - Estrutura Detalhada dos Sub-Nós: Ao criar os sub-nós, é importante garantir uma estrutura detalhada e organizada que forneça informações ricas e úteis aos alunos. Recomenda-se incluir sub-nós que abordem diferentes aspectos ou temas relacionados ao tópico principal. Por exemplo, você pode criar sub-nós para explorar causas, consequências, eventos históricos relevantes, pessoas envolvidas, conceitos-chave e assim por diante. Dentro de cada sub-nó, adicione vários outros nós explicativos que detalhem e explorem mais a fundo os aspectos específicos do tema. Isso ajudará os alunos a obterem uma compreensão mais completa e aprofundada do assunto, proporcionando uma visão abrangente e enriquecedora da matéria.
"""

def get_mind_map_prompt():
   return f"""
   Você é um professor e deseja criar um mapa mental para auxiliar os alunos nos estudos.
   Crie um mapa mental com o assunto abordado 
   Regras:

   {rules}
    
   JSON de entrada de exemplo:

   {input_example}

   Retorne o mapa mental em formato JSON.

   Exemplo de retorno:

   {output_example}
   
   """
   