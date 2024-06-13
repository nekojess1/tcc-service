input_example = """
    {
      "subject": "{subject}",
      "language": "{response idiom}"
    }
    """
    
output_example = """
{
  "nodes": [
    { "id": "0", "description": "<Segunda Guerra Mundial>" },
    { "id": "1", "description": "<Causas da Guerra>" },
    { "id": "2", "description": "<Tratado de Versalhes<BR/>Reparações econômicas<BR/>Perda de territórios>" },
    { "id": "3", "description": "<Ascensão do Nazismo e Fascismo<BR/>Alemanha: Adolf Hitler<BR/>Itália: Benito Mussolini>" },
    { "id": "4", "description": "<Expansionismo Japonês<BR/>Invasão da Manchúria<BR/>Guerra Sino-Japonesa>" },
    { "id": "5", "description": "<Fracasso da Liga das Nações<BR/>Incapacidade de manter a paz>" },
    { "id": "6", "description": "<Política de Apaziguamento<BR/>Concessões às demandas de Hitler>" },
    { "id": "7", "description": "<Principais Acontecimentos>" },
    { "id": "8", "description": "<Início da Guerra (1939)<BR/>Invasão da Polônia pela Alemanha>" },
    { "id": "9", "description": "<Batalhas e Campanhas Importantes<BR/>Batalha da França<BR/>Batalha da Grã-Bretanha<BR/>Operação Barbarossa (Invasão da União Soviética)<BR/>Ataque a Pearl Harbor<BR/>Batalha de Stalingrado<BR/>Desembarque da Normandia (Dia D)<BR/>Batalha de Midway>" },
    { "id": "10", "description": "<Holocausto<BR/>Campos de concentração e extermínio<BR/>Genocídio de judeus e outras minorias>" },
    { "id": "11", "description": "<Alianças e Lados Opositores>" },
    { "id": "12", "description": "<Aliados<BR/>Estados Unidos<BR/>União Soviética<BR/>Reino Unido<BR/>França>" },
    { "id": "13", "description": "<Eixo<BR/>Alemanha<BR/>Itália<BR/>Japão>" },
    { "id": "14", "description": "<Tecnologia e Armas>" },
    { "id": "15", "description": "<Armas Nucleares<BR/>Projetos Manhattan>" },
    { "id": "16", "description": "<Aviões e Tanques<BR/>Desenvolvimento de aviões de combate<BR/>Evolução dos tanques de guerra>" },
    { "id": "17", "description": "<Comunicações e Criptografia<BR/>Código Enigma<BR/>Máquinas de decifração (Bletchley Park)>" },
    { "id": "18", "description": "<Consequências da Guerra>" },
    { "id": "19", "description": "<Perdas Humanas e Destruição<BR/>Vítimas civis e militares<BR/>Devastação de cidades>" },
    { "id": "20", "description": "<Tribunal de Nuremberg<BR/>Julgamento de crimes de guerra>" },
    { "id": "21", "description": "<Criação da ONU<BR/>Objetivo de promover a paz mundial>" },
    { "id": "22", "description": "<Guerra Fria<BR/>Divisão entre blocos capitalista (EUA) e socialista (URSS)>" },
    { "id": "23", "description": "<Reconfiguração Geopolítica<BR/>Divisão da Alemanha<BR/>Novas fronteiras na Europa e Ásia>" },
    { "id": "24", "description": "<Personagens Importantes>" },
    { "id": "25", "description": "<Líderes dos Aliados<BR/>Franklin D. Roosevelt (EUA)<BR/>Winston Churchill (Reino Unido)<BR/>Joseph Stalin (URSS)>" },
    { "id": "26", "description": "<Líderes do Eixo<BR/>Adolf Hitler (Alemanha)<BR/>Benito Mussolini (Itália)<BR/>Hirohito (Japão)>" },
    { "id": "27", "description": "<Outros Personagens Relevantes<BR/>Dwight D. Eisenhower (Comandante Supremo Aliado)<BR/>Erwin Rommel (Marechal Alemão)<BR/>Anne Frank (Símbolo das vítimas do Holocausto)>" },
    { "id": "28", "description": "<Cronologia da Guerra>" },
    { "id": "29", "description": "<1939-1940: Início e Guerra Relâmpago (Blitzkrieg)>" },
    { "id": "30", "description": "<1941-1942: Expansão do Eixo e Entrada dos EUA>" },
    { "id": "31", "description": "<1943: Virada dos Aliados>" },
    { "id": "32", "description": "<1944: Avanço dos Aliados>" },
    { "id": "33", "description": "<1945: Fim da Guerra e Rendição dos Eixos>" }
  ],
  "edges": [
    { "from_node": "0", "to_node": "1" },
    { "from_node": "0", "to_node": "7" },
    { "from_node": "0", "to_node": "11" },
    { "from_node": "0", "to_node": "14" },
    { "from_node": "0", "to_node": "18" },
    { "from_node": "0", "to_node": "24" },
    { "from_node": "0", "to_node": "28" },
    { "from_node": "1", "to_node": "2" },
    { "from_node": "1", "to_node": "3" },
    { "from_node": "1", "to_node": "4" },
    { "from_node": "1", "to_node": "5" },
    { "from_node": "1", "to_node": "6" },
    { "from_node": "7", "to_node": "8" },
    { "from_node": "7", "to_node": "9" },
    { "from_node": "7", "to_node": "10" },
    { "from_node": "11", "to_node": "12" },
    { "from_node": "11", "to_node": "13" },
    { "from_node": "14", "to_node": "15" },
    { "from_node": "14", "to_node": "16" },
    { "from_node": "14", "to_node": "17" },
    { "from_node": "18", "to_node": "19" },
    { "from_node": "18", "to_node": "20" },
    { "from_node": "18", "to_node": "21" },
    { "from_node": "18", "to_node": "22" },
    { "from_node": "18", "to_node": "23" },
    { "from_node": "24", "to_node": "25" },
    { "from_node": "24", "to_node": "26" },
    { "from_node": "24", "to_node": "27" },
    { "from_node": "28", "to_node": "29" },
    { "from_node": "28", "to_node": "30" },
    { "from_node": "28", "to_node": "31" },
    { "from_node": "28", "to_node": "32" },
    { "from_node": "28", "to_node": "33" }
  ]
}
"""

rules = """
      1. Ao criar a descrição, caso seja extensa, use <BR/> para quebrar o texto e facilitar a visualização.
      2. Envolva o texto da descrição com tags HTML, como "<Subtópico 1<BR/>com mais texto>".
      3. O Mapa mental deve ter no máximo 10 níveis 
      4. O idioma usado para criar a resposta está explícito no campo "language". Caso ele venha vazio, utilize o padrão "EN-US".
      5. Ao pesquisar sobre o assunto, divida-o em diversos tópicos, cada um representado como um nó no mapa mental.
     
"""

def get_mind_map_prompt():
   return f"""
   Você é um professor e deseja criar um mapa mental para auxiliar os alunos nos estudos.
   Crie um mapa mental completo e detalhado do assunto no campo "subject"
   
   Regras:

   {rules}
    
   JSON de entrada de exemplo:

   {input_example}

   Retorne o mapa mental em formato JSON.

   Exemplo de retorno:

   {output_example}
   
   """
   