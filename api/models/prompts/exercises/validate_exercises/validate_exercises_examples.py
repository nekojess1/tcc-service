# Input Format
input_format = """
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
    }
  ]
}
"""

# Output Format
output_format = """
{
    "questions": [
        {
            "title": "{Question Title}",
            "level": 2,  # Difficulty level (1 = Easy, 2 = Medium, 3 = Hard)
            "motive": "{Evaluation Motive}"  # Reason for the assigned difficulty level
        }
    ],
    "hard_questions_quantity": 0,  # Total number of hard questions
    "medium_questions_quantity": 1,  # Total number of medium questions
    "easy_questions_quantity": 0,  # Total number of easy questions
    "average_difficulty": 2.0  # Average difficulty level (rounded to nearest whole number)
}
"""

# Input Example
input_example = """
{
  "exercises": [
    {
      "topic": "Genetics",
      "questions": [
        {
          "type": "multiple_choice",
          "question": "What is the basic unit of heredity?",
          "options": [
            "Gene",
            "Chromosome",
            "DNA",
            "Protein",
            "Cell"
          ],
          "answer": "Gene",
          "hints": null
        }
      ]
    }
  ]
}
"""

# Output Example
output_example = """
{
    "questions": [
        {
            "title": "Explain the main causes that led to the beginning of World War II.",
            "level": 2,
            "motive": "Requires a detailed explanation and intermediate historical analysis."
        }
    ],
    "hard_questions_quantity": 0,
    "medium_questions_quantity": 1,
    "easy_questions_quantity": 0,
    "average_difficulty": 2.0
}
"""
