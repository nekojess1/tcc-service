input_format = """
{
      "title": "{question title}",
      "choices": [optional question choices]
    }
"""

output_format = """
{
    "questions": [
        {
            "title": "{Question Title}",
            "level": 2,
            "motive": "{Avaliation Motive}"
        }
    ],
    "hard_questions_quantity": 0,
    "medium_questions_quantity": 1,
    "easy_questions_quantity": 0,
    "average_difficulty": 2.0
}
"""

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

output_example = """"
{
    "questions": [
        {
            "title": "Explique as principais causas que levaram ao início da Segunda Guerra Mundial.",
            "level": 2,
            "motive": "Requer uma explicação detalhada e uma análise histórica intermediária."
        }
    ],
    "hard_questions_quantity": 0,
    "medium_questions_quantity": 1,
    "easy_questions_quantity": 0,
    "average_difficulty": 2.0
}

"""

