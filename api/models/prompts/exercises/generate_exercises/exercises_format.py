input_format = """
{
  "topic": {
    "name": "{question_subject}",
    "number_of_questions": {number_of_questions},
    "multiple_choice_qty": {multiple_choice_qty},
    "multiple_choice_options": {multiple_choice_options},
    "open_ended_qty": {open_ended_qty}
  },
  "idiom": "{idiom}",
  "difficulty": "{difficulty}"
}
"""

output_format = """
{
  "topic": "{topic}",
  "questions": [
    {
      "type": "multiple_choice",
      "question": "{multiple_choice_question}",
      "options": [
        "{option_1}",
        "{option_2}",
        "{option_3}",
        "{option_4}"
        "{option_5}"
      ],
      "answer": "{correct_option}"
    },
    {
      "type": "open_ended",
      "question": "{open_ended_question}",
      "options": [],  
      "answer": "{model_answer}"
    }
  ]
}
"""

