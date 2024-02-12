output_example = """
{
  "nodes": [
    { "id": "0", "content": "Resumos" },
    { "id": "1", "content": "Segunda Guerra Mundial" },
    { "id": "2", "content": "Motivos e Causas" },
    { "id": "3", "content": "Disputas Territoriais e rivalidades políticas" },
    { "id": "4", "content": "Ideologias conflitantes, como o nazismo e o fascismo" },
    { "id": "5", "content": "Estopim" },
    { "id": "6", "content": "Invasão da Polônia pela Alemanha nazista" },
    { "id": "7", "content": "Duração" }
    { "id": "8", "content": "Seis anos de conflito, de 1939 a 1945." }
    { "id": "9", "content": "1939: Início com invasão da polônia pela Alemanha" },
    { "id": "10", "content": "1941: Entrada dos EUA após o ataque a Pearl Harbor" },
    { "id": "11", "content": "1945: Rendição da Alemanha e do Japão" }
    { "id": "12", "content": "Principais Eventos" }
    { "id": "13", "content": "Ataque japonês a Pearl Harbor, em dezembro de 1941." }
    { "id": "14", "content": "Batalha de Stalingrado e Batalha de Kursk, no leste europeu." },
    { "id": "15", "content": "Consequências" },
    { "id": "16", "content": "Alemanha repartida entre os aliados" }
    { "id": "17", "content": "Guerra Fria entre EUA e URSS" }
    { "id": "18", "content": "Criação das Nações unidass" }
    { "id": "19", "content": "Guerra Fria" },
    { "id": "20", "content": "O que foi?" },
    { "id": "21", "content": "Conflito ideológico e político entre Estados Unidos e União Soviética" },
    { "id": "22", "content": "Período de tensão e rivalidade entre as superpotências mundiais" },
    { "id": "23", "content": "Causou" },
    { "id": "24", "content": "Corrida Armamentista" },
    { "id": "25", "content": "Desenvolvimento de armas nucleares e estratégias de dissuasão" },
    { "id": "26", "content": "Consequências" },
    { "id": "27", "content": "Queda da União Soviética em 1991" },
    { "id": "28", "content": "Ascensão dos Estados Unidos como superpotência dominante" },
    { "id": "29", "content": "Queda do Muro de Berlim em 1989" }



  ],
  "edges": [
    { "source": "0", "target": "1"},
    { "source": "1", "target": "2"},
    { "source": "1", "target": "5"},
    { "source": "1", "target": "7"},
    { "source": "1", "target": "12"},
    { "source": "1", "target": "15"},
    { "source": "2", "target": "3"},
    { "source": "2", "target": "4"},
    { "source": "5", "target": "6"},
    { "source": "7", "target": "8"},
    { "source": "7", "target": "9"},
    { "source": "7", "target": "10"},
    { "source": "7", "target": "11"},
    { "source": "12", "target": "13"},
    { "source": "12", "target": "14"},
    { "source": "15", "target": "16"},
    { "source": "15", "target": "17"},
    { "source": "15", "target": "18"},
    { "source": "0", "target": "19"},
    { "source": "19", "target": "20"},
    { "source": "19", "target": "23"},
    { "source": "19", "target": "26"},
    { "source": "19", "target": "17"},
    { "source": "20", "target": "21"},
    { "source": "20", "target": "22"},
    { "source": "23", "target": "24"},
    { "source": "23", "target": "25"},
    { "source": "26", "target": "27"},
    { "source": "26", "target": "28"},
    { "source": "26", "target": "29"},
    { "source": "28", "target": "16"},
  ]
}

"""

input_example = """
{
   "perguntas":[
      {
         "titulo":"{título da pergunta}",
         "respostas dos alunos":[
            {
               "resposta":"{resposta da pergunta}",
               "marcadores":[
                  {
                     "tipo":"{acerto, acerto parcial ou erro}",
                     "nome":"{trecho da resposta ao qual se refere o marcador}"
                  }
               ],
               "feedback":"{feedback do professor}"
            }
         ]
      }
   ]
}
"""

def get_mind_map_prompt():
   return f"""
   Você é um professor e deseja criar um mapa mental para auxiliar os alunos nos estudos.
   Você deverá seguir essas regras abaixo para gerar o grafo:

   1 - Você receberá uma lista de perguntas e respostas dos alunos 
   2 - Você observará as perguntas que mais tiverem respostas marcadas como "erro" ou "acerto parcial"
   3 - Você armazenará os temas das perguntas que os alunos mais estão errando.
   4 - Você fará uma pesquisa sobre os temas armazenados e coletará informações relevantes sobre eles. 
   5 - Não é necessário se limitar ao tamanho dos textos do mapa mental.
   6 - As respostas dos alunos nunca podem ser usadas como conteúdo no mapa mental
   7 - Você nunca deve colocar conteúdo incorreto no mapa mental, somente os corretos, pois vão servir de estudo para os alunos
   8 - O grafo deverá ter até no máximo 3 níveis 
   9 - No grafo, quando tiver assuntos interligados, os mesmos devem ter um nó entre eles; 
   10 - Explore a possibilidade de conexões entre diferentes temas no grafo, independentemente de terem o mesmo ponto de origem.
   12 - Ao fazer a pesquisa, você deve escrever textos sobre cada conteúdo, e tirar os principais trechos dele para resumi-lo, seguindo o exemplo de saída.
   13 - Você deverá adicionar tópicos que marcam o assunto, exemplo: Causa, Consequência, Ínicio, Desfecho. E assim, ligar novos nós a esses nó. 
   14 - Não se limite a escrever sobre um assunto, pegue os principais pontos sobre cada assunto e coloque no mapa mental. 
   
   Esse json vai ser o seu exemplo de entrada:

   {input_example}


   Você deverá retornar com o mapa mental em formato de json.

   Modelo de retorno:
   
   {output_example}


   """