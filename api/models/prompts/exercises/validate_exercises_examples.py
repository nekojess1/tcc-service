# Input Format
input_format = """
{
    "title": "{question title}",
    "choices": [  # optional question choices
        # Example of choices:
        # "Option 1",
        # "Option 2"
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
    "title": "What characteristic distinguishes bryophytes from vascular plants?",
    "choices": [
        "Presence of true roots",
        "Absence of seeds and flowers",
        "Dominant diploid sporophyte stage",
        "Vascular tissue for water transport",
        "Flowering reproductive structures"
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
