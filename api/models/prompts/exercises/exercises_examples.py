input_example = """
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

output_example = """
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

