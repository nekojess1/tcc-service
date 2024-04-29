input_format = """

{
  "topics": [
    {
      "name": "{question subject}",
      "number_of_questions": 3,
      "multiple_choice_qty": 2,
      "multiple_choice_options":5,
      "open_ended_qty": 1,
      "difficulty": "avançado"
    }
  ]
}

"""

output_format = """

{
  "exercises": [
    {
      "topic": "Nome do Tópico Aqui",
      "questions": [
        {
          "type": "multiple_choice",
          "question": "Inserir a pergunta de múltipla escolha aqui.",
          "options": ["Opção 1", "Opção 2", "Opção 3", "Opção 4"],
          "answer": "Inserir a resposta correta aqui"
        },
        {
          "type": "multiple_choice",
          "question": "Inserir outra pergunta de múltipla escolha aqui.",
          "options": ["Opção 1", "Opção 2", "Opção 3", "Opção 4"],
          "answer": "Inserir a resposta correta aqui"
        },
        {
          "type": "open_ended",
          "question": "Inserir a pergunta aberta aqui.",
          "hints": ["Inserir dica(s) para resolver a pergunta, se necessário."],
          "answer": "Inserir a resposta correta aqui"
        }
      ]
    },
    {
      "topic": "Outro Nome de Tópico Aqui",
      "questions": [
        {
          "type": "multiple_choice",
          "question": "Inserir a pergunta de múltipla escolha aqui.",
          "options": ["Opção 1", "Opção 2", "Opção 3", "Opção 4"],
          "answer": "Inserir a resposta correta aqui"
        },
        {
          "type": "open_ended",
          "question": "Inserir a pergunta aberta aqui.",
          "hints": ["Inserir dica(s) para resolver a pergunta, se necessário."],
          "answer": "Inserir a resposta correta aqui"
        }
      ]
    }
  ]
}

"""

context = """

Como professor responsável por criar exercícios estimulantes e educativos para estudantes, siga estas diretrizes para a criação de tais exercícios:

1. Respeite o número de questões recebido, gerando apenas essa quantidade de questões.
2. Respeite a quantidade de questões abertas e de questões fechadas estipuladas.
3. Respeite a quantidade de alternativas em cada questão fechada.
4. É possível receber vários tópicos, e para cada tópico, especifique o assunto, quantidade total de questões, quantidade de questões abertas, quantidade de questões fechadas, quantidade de alternativas possíveis na questão fechada e a dificuldade das questões.
5. Respeite a dificuldade de cada questão, seguindo estas diretrizes:
   
   - Fácil:
     - Conceitos básicos e diretos.
     - Um passo simples para resolver.
     - Respostas encontradas nos materiais de estudo.
     - Sem exigir conhecimento prévio avançado.

   - Intermediário:
     - Compreensão mais aprofundada do conceito.
     - Múltiplos passos ou etapas para resolver.
     - Alguma análise ou aplicação do conhecimento.
     - Podem envolver conexões entre conceitos diferentes.

   - Difícil:
     - Entendimento profundo e crítico do assunto.
     - Múltiplos conceitos ou técnicas complexas.
     - Raciocínio abstrato ou pensamento criativo para resolver.
     - Respostas não óbvias e requerem abordagem analítica.

"""

def get_exercise_prompt():
    """Generate an exercise with differents subjects"""

    return f"""

    {context}

    Exemplo de Retorno JSON:

    {output_format}
    
    """
