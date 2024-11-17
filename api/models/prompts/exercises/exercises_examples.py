input_format = """
{
  "topics": [
    {
      "name": "{question subject}",
      "number_of_questions": {number of questions about the topic},
      "multiple_choice_qty": {number of multiple-choice questions},
      "multiple_choice_options": {number of options per multiple-choice question},
      "open_ended_qty": {number of open-ended questions},
      "difficulty": {difficulty of the questions} 
    }
  ],
  "questions_example": [{optional field containing example exercises}]
}
"""

output_format = """
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
"""

output_example = """"
{
  "exercises": [
    {
      "topic": "Geometria",
      "questions": [
        {
          "type": "multiple_choice",
          "question": "Qual é a fórmula para calcular a área de um triângulo?",
          "options": [
            "A = base × altura",
            "A = lado × lado",
            "A = 2 × π × raio",
            "A = comprimento × largura"
          ],
          "answer": "A = base × altura"
        },
        {
          "type": "open_ended",
          "question": "Explique como você pode usar o teorema de Pitágoras para encontrar a hipotenusa de um triângulo retângulo.",
          "answer": "Para encontrar a hipotenusa, eu uso a fórmula a² + b² = c², onde a e b são os catetos e c é a hipotenusa."
        }
      ]
    },
    {
      "topic": "História",
      "questions": [
        {
          "type": "multiple_choice",
          "question": "Qual evento marcou o início da Revolução Francesa?",
          "options": [
            "A Queda da Bastilha",
            "A assinatura da Declaração de Independência",
            "A Revolução Industrial",
            "A Guerra dos Cem Anos"
          ],
          "answer": "A Queda da Bastilha"
        },
        {
          "type": "open_ended",
          "question": "Discuta as causas da Revolução Francesa.",
          "hints": ["Considere fatores sociais, econômicos e políticos."],
          "answer": "As causas da Revolução Francesa incluem a desigualdade social entre os três estados, a crise financeira do governo e a influência das ideias iluministas."
        }
      ]
    }
  ]
}


"""

