input_format = """
{
  "questions": [
    {
      "title": "string",
      "question_id": "string",
      "response": {
        "answer": "string",
        "response_id": "string",
        "type": ""
      }
    }
  ]
}
    """
    
input_example = """
{
  "questions": [
    {
      "title": "Função principal do sistema respiratório",
      "question_id": "q1",
      "response": {
        "answer": "A principal função do sistema respiratório é fornecer oxigênio ao corpo e remover dióxido de carbono.",
        "response_id": "r1",
        "type": "acerto"
      }
    },
    {
      "title": "Componentes do sistema respiratório",
      "question_id": "q2",
      "response": {
        "answer": "Os principais componentes do sistema respiratório incluem o nariz, faringe, laringe, traqueia, brônquios e pulmões.",
        "response_id": "r2",
        "type": "acerto"
      }
    },
    {
      "title": "Diferença entre respiração pulmonar e respiração celular",
      "question_id": "q3",
      "response": {
        "answer": "A respiração pulmonar envolve a troca de gases (oxigênio e dióxido de carbono) entre o ambiente e os pulmões, enquanto a respiração celular ocorre dentro das células, utilizando oxigênio para produzir energia a partir de nutrientes.",
        "response_id": "r3",
        "type": "acerto parcial"
      }
    },
    {
      "title": "O que é o diafragma e sua função",
      "question_id": "q4",
      "response": {
        "answer": "O diafragma é um músculo em forma de cúpula localizado abaixo dos pulmões que ajuda na respiração, contraindo-se para permitir a entrada de ar nos pulmões e relaxando para expulsá-lo.",
        "response_id": "r4",
        "type": "acerto"
      }
    },
    {
      "title": "Doenças comuns do sistema respiratório",
      "question_id": "q5",
      "response": {
        "answer": "Algumas doenças comuns do sistema respiratório incluem asma, bronquite, pneumonia e doença pulmonar obstrutiva crônica (DPOC).",
        "response_id": "r5",
        "type": "acerto"
      }
    },
    {
      "title": "O papel do sistema circulatório no sistema respiratório",
      "question_id": "q6",
      "response": {
        "answer": "O sistema circulatório trabalha em conjunto com o sistema respiratório para transportar oxigênio dos pulmões para as células do corpo e remover dióxido de carbono das células para os pulmões.",
        "response_id": "r6",
        "type": "acerto"
      }
    },
    {
      "title": "Como a troca gasosa ocorre nos alvéolos",
      "question_id": "q7",
      "response": {
        "answer": "A troca gasosa nos alvéolos ocorre por difusão, onde o oxigênio passa dos alvéolos para o sangue e o dióxido de carbono passa do sangue para os alvéolos.",
        "response_id": "r7",
        "type": "acerto"
      }
    },
    {
      "title": "O impacto do tabagismo no sistema respiratório",
      "question_id": "q8",
      "response": {
        "answer": "O tabagismo pode causar danos aos pulmões e às vias respiratórias, levando a doenças como enfisema, bronquite crônica e câncer de pulmão.",
        "response_id": "r8",
        "type": "acerto"
      }
    },
    {
      "title": "Como a respiração é controlada pelo sistema nervoso",
      "question_id": "q9",
      "response": {
        "answer": "A respiração é controlada pelo bulbo e pela ponte no cérebro, que enviam sinais aos músculos respiratórios para regular a frequência e a profundidade da respiração.",
        "response_id": "r9",
        "type": "acerto parcial"
      }
    },
    {
      "title": "A função do muco nas vias respiratórias",
      "question_id": "q10",
      "response": {
        "answer": "O muco nas vias respiratórias ajuda a capturar e remover partículas de poeira, bactérias e outros contaminantes do ar inalado.",
        "response_id": "r10",
        "type": "acerto"
      }
    },
    {
      "title": "Os pulmões são responsáveis pela digestão de alimentos",
      "question_id": "q11",
      "response": {
        "answer": "Os pulmões são responsáveis pela troca de gases, não pela digestão de alimentos, que é função do sistema digestivo.",
        "response_id": "r11",
        "type": "erro"
      }
    },
    {
      "title": "A respiração celular ocorre nos pulmões",
      "question_id": "q12",
      "response": {
        "answer": "A respiração celular ocorre dentro das células, utilizando oxigênio para produzir energia a partir de nutrientes, e não nos pulmões.",
        "response_id": "r12",
        "type": "erro"
      }
    },
    {
      "title": "O diafragma é um osso que protege os pulmões",
      "question_id": "q13",
      "response": {
        "answer": "O diafragma é um músculo, não um osso, que ajuda na respiração ao se contrair e relaxar para permitir a entrada e saída de ar nos pulmões.",
        "response_id": "r13",
        "type": "erro"
      }
    },
    {
      "title": "A DPOC é causada por vírus",
      "question_id": "q14",
      "response": {
        "answer": "A DPOC (doença pulmonar obstrutiva crônica) é geralmente causada por exposição prolongada a irritantes que danificam os pulmões e as vias respiratórias, como fumaça de cigarro, e não por vírus.",
        "response_id": "r14",
        "type": "erro"
      }
    },
    {
      "title": "O sistema nervoso não tem influência na respiração",
      "question_id": "q15",
      "response": {
        "answer": "O sistema nervoso controla a respiração através do bulbo e da ponte no cérebro, regulando a frequência e a profundidade da respiração.",
        "response_id": "r15",
        "type": "erro"
      }
    }
  ]
}
"""
  
output_example = """
{
  "nodes": [
    { "id": "0", "description": "Sistema Respiratório", "is_common_error": false },
    { "id": "1", "description": "Função Principal", "is_common_error": false },
    { "id": "2", "description": "O sistema respiratório é responsável por fornecer oxigênio ao corpo e remover dióxido de carbono.", "is_common_error": false },
    { "id": "3", "description": "Equilíbrio ácido-base do sangue", "is_common_error": false },
    { "id": "4", "description": "Componentes", "is_common_error": false },
    { "id": "5", "description": "Nariz", "is_common_error": false },
    { "id": "6", "description": "Filtra, aquece e umedece o ar inalado.", "is_common_error": false },
    { "id": "7", "description": "Faringe", "is_common_error": false },
    { "id": "8", "description": "Passagem comum para ar e alimentos.", "is_common_error": false },
    { "id": "9", "description": "Laringe", "is_common_error": false },
    { "id": "10", "description": "Contém as cordas vocais e protege as vias aéreas inferiores.", "is_common_error": false },
    { "id": "11", "description": "Traqueia", "is_common_error": false },
    { "id": "12", "description": "Tubo que conduz o ar da laringe aos brônquios.", "is_common_error": false },
    { "id": "13", "description": "Brônquios", "is_common_error": false },
    { "id": "14", "description": "Ramificações que conduzem o ar aos pulmões.", "is_common_error": false },
    { "id": "15", "description": "Pulmões", "is_common_error": false },
    { "id": "16", "description": "Órgãos onde ocorrem as trocas gasosas.", "is_common_error": false },
    { "id": "17", "description": "Troca Gasosa", "is_common_error": false },
    { "id": "18", "description": "Ocorrência nos alvéolos", "is_common_error": false },
    { "id": "19", "description": "Oxigênio e dióxido de carbono", "is_common_error": false },
    { "id": "20", "description": "Doenças Comuns", "is_common_error": false },
    { "id": "21", "description": "Asma", "is_common_error": false },
    { "id": "22", "description": "Inflamação e estreitamento das vias aéreas.", "is_common_error": false },
    { "id": "23", "description": "Bronquite", "is_common_error": false },
    { "id": "24", "description": "Inflamação dos brônquios, geralmente causada por infecção ou irritação.", "is_common_error": false },
    { "id": "25", "description": "Pneumonia", "is_common_error": false },
    { "id": "26", "description": "Infecção que inflama os sacos de ar nos pulmões.", "is_common_error": false },
    { "id": "27", "description": "DPOC", "is_common_error": false },
    { "id": "28", "description": "Doença Pulmonar Obstrutiva Crônica.", "is_common_error": false },
    { "id": "29", "description": "Respiração Celular", "is_common_error": false },
    { "id": "30", "description": "Ocorrência nas mitocôndrias", "is_common_error": false },
    { "id": "31", "description": "Produção de energia (ATP) e subproduto (dióxido de carbono)", "is_common_error": false },
    { "id": "32", "description": "Diafragma", "is_common_error": false },
    { "id": "33", "description": "Músculo em forma de cúpula", "is_common_error": false },
    { "id": "34", "description": "Função durante a inalação e exalação", "is_common_error": false },
    { "id": "35", "description": "Impacto do Tabagismo", "is_common_error": false },
    { "id": "36", "description": "Danos significativos ao sistema respiratório", "is_common_error": false },
    { "id": "37", "description": "Enfisema", "is_common_error": false },
    { "id": "38", "description": "Destruição dos alvéolos.", "is_common_error": false },
    { "id": "39", "description": "Bronquite Crônica", "is_common_error": false },
    { "id": "40", "description": "Inflamação persistente dos brônquios.", "is_common_error": false },
    { "id": "41", "description": "Câncer de Pulmão", "is_common_error": false },
    { "id": "42", "description": "Crescimento descontrolado de células malignas.", "is_common_error": false },
    { "id": "43", "description": "Controle da Respiração", "is_common_error": false },
    { "id": "44", "description": "Centros respiratórios no cérebro", "is_common_error": false },
    { "id": "45", "description": "Regulação da frequência e profundidade respiratória", "is_common_error": false },
    { "id": "46", "description": "Sistema Circulatório", "is_common_error": false },
    { "id": "47", "description": "Transporte de oxigênio e remoção de dióxido de carbono", "is_common_error": false },
    { "id": "48", "description": "Função do Muco", "is_common_error": false },
    { "id": "49", "description": "Captura e remoção de partículas de poeira e bactérias", "is_common_error": false },
    { "id": "50", "description": "Função dos Pulmões", "is_common_error": true },
    { "id": "51", "description": "Os pulmões são responsáveis pelas trocas gasosas no corpo humano, onde o oxigênio é absorvido e o dióxido de carbono é liberado.", "is_common_error": true },
    { "id": "52", "description": "Local da Respiração Celular", "is_common_error": true },
    { "id": "53", "description": "A respiração celular ocorre nas mitocôndrias das células, onde a glicose e o oxigênio são utilizados para produzir energia (ATP).", "is_common_error": true },
    { "id": "54", "description": "Natureza do Diafragma", "is_common_error": true },
    { "id": "55", "description": "O diafragma é um músculo em forma de cúpula que desempenha um papel crucial na respiração, contraindo-se para permitir a entrada de ar nos pulmões.", "is_common_error": true },
    { "id": "56", "description": "Causa da DPOC", "is_common_error": true },
    { "id": "57", "description": "A Doença Pulmonar Obstrutiva Crônica (DPOC) é causada principalmente por exposição prolongada a irritantes, como a fumaça do cigarro.", "is_common_error": true },
    { "id": "58", "description": "Influência do Sistema Nervoso", "is_common_error": true },
    { "id": "59", "description": "O sistema nervoso controla a respiração através dos centros respiratórios localizados no bulbo e na ponte, que regulam a frequência e a profundidade da respiração.", "is_common_error": true }
  ],
  "edges": [
    { "from_node": "0", "to_node": "1" },
    { "from_node": "0", "to_node": "4" },
    { "from_node": "1", "to_node": "2" },
    { "from_node": "1", "to_node": "3" },
    { "from_node": "4", "to_node": "5" },
    { "from_node": "4", "to_node": "7" },
    { "from_node": "4", "to_node": "9" },
    { "from_node": "4", "to_node": "11" },
    { "from_node": "4", "to_node": "13" },
    { "from_node": "4", "to_node": "15" },
    { "from_node": "5", "to_node": "6" },
    { "from_node": "7", "to_node": "8" },
    { "from_node": "9", "to_node": "10" },
    { "from_node": "11", "to_node": "12" },
    { "from_node": "13", "to_node": "14" },
    { "from_node": "15", "to_node": "17" },
    { "from_node": "17", "to_node": "18" },
    { "from_node": "17", "to_node": "19" },
    { "from_node": "20", "to_node": "21" },
    { "from_node": "20", "to_node": "23" },
    { "from_node": "20", "to_node": "25" },
    { "from_node": "20", "to_node": "27" },
    { "from_node": "29", "to_node": "30" },
    { "from_node": "29", "to_node": "31" },
    { "from_node": "32", "to_node": "33" },
    { "from_node": "32", "to_node": "34" },
    { "from_node": "35", "to_node": "36" },
    { "from_node": "35", "to_node": "37" },
    { "from_node": "35", "to_node": "39" },
    { "from_node": "35", "to_node": "41" },
    { "from_node": "43", "to_node": "44" },
    { "from_node": "43", "to_node": "45" },
    { "from_node": "46", "to_node": "47" },
    { "from_node": "48", "to_node": "49" },
    { "from_node": "15", "to_node": "50" },
    { "from_node": "50", "to_node": "51" },
    { "from_node": "29", "to_node": "52" },
    { "from_node": "52", "to_node": "53" },
    { "from_node": "32", "to_node": "54" },
    { "from_node": "54", "to_node": "55" },
    { "from_node": "27", "to_node": "56" },
    { "from_node": "56", "to_node": "57" },
    { "from_node": "43", "to_node": "58" },
    { "from_node": "58", "to_node": "59" }
  ]
}

"""

rules = """  
  1 - Se identificar alguma questão com "type" erro ou acerto parcial, o campo "is_common_error" deverá ser true
  2 - Quebre ao máximo os assuntos em outros nós, para que a descrição não fique muito extensa e seja mais fácil de visualizar
  3 - Nunca utilize as respostas dos alunos como conteúdo para o mapa mental.
  4 - Certifique-se da credibilidade do texto antes de incluí-lo no mapa.
  5 - Divida os assuntos em diversos subtópicos, quanto mais subtópicos, melhor detalhe.
  6 - Explore ao máximo o tema e o divida em subtemas diversos, permitindo múltiplos níveis de profundidade conforme necessário.
  7 - Garanta uma estrutura detalhada e organizada que forneça informações ricas e úteis aos alunos.
  8 - Um nó sempre deve ter pelo menos um outro nó o ligando, não podem nunca não ter ligação.
  9 - O primeiro nó deve ser o tema central, ou "Conceitos Gerais" se os temas forem diferentes.
  10  - Um grafo sempre deve ter pelo menos uma aresta.
  11 - Verifique todas as possíveis relações entre os tópicos do exercício e adicione arestas entre eles.
  12 - Ao criar a descrição, caso seja extensa, use `<BR/>` para quebrar e facilitar a visualização.
  13 - Envolva o texto da descrição com tags HTML, como "<Subtópico 1<BR/>com mais texto>".
  14 - Não usar o termo "erro comum" no mapa mental. Somente mostre os assuntos.
"""

def get_mind_map_prompt():
   return f"""
   Você é um professor e deseja criar um mapa mental para auxiliar os alunos nos estudos. 
   Você receberá uma lista de perguntas com a devida resposta do aluno. Você usará essa lista para
   fazer um mapa mental com os assuntos abordados. 

   Siga essas regras para gerar o mapa mental:

   {rules}
    
   JSON de entrada de exemplo:

   {input_format}

   Retorne o mapa mental em formato JSON.
   
   exemplos de entrada:
   
   {input_example}
   
   exemplo de saída:
   
   {output_example}
   
   """
   