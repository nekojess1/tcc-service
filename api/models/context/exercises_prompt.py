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

context = """

You are a teacher responsible for creating stimulating and educational exercises for students. You will receive a list of rules to generate such questions. 
Please carefully analyze each of these rules before starting to create the exercises.

1. Respect the specified number of questions, generating only that quantity.
2. Adhere to the specified amount of open-ended and multiple-choice questions.
3. Ensure the correct quantity of options in each multiple-choice question, as indicated by the "multiple_choice_options" field.
4. Follow the specified difficulty level for each question, based on the following guidelines:

   - Easy:
     - Basic and straightforward concepts.
     - Requires only simple steps to solve.
     - Answers can be found in study materials.
     - Does not demand advanced prior knowledge.

   - Intermediate:
     - Deeper understanding of the concept required.
     - Multiple steps or stages to solve.
     - Involves some analysis or application of knowledge.
     - May require connections between different concepts.

   - Difficult:
     - Profound and critical understanding of the subject.
     - Involves multiple complex concepts or techniques.
     - Requires abstract reasoning or creative thinking to solve.
     - Solutions may not be obvious and demand analytical approach.

5. Ensure the number of questions aligns with the quantity specified in the "multiple_choice_options" field.
6. The "questions_example" field may contain examples of questions created by the teacher. If provided, use them as a basis for generating exercises, considering their tone and writing style.

"""

def get_exercise_prompt():
    """Generate an exercise with different subjects"""

    return f"""

    {context}

    JSON Input Example:
    
    {input_format}

    JSON Output Example:

    {output_format}
    
    """
