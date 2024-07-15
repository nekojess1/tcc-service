input_example = """
{
    "daysDuration": "{total number of available study days}",
    "daysOfWeek": [
        "days of the week available for study, such as Monday, Tuesday"
    ],
    "hoursPerDay": "{available study hours per day}",
    "topics": ["list of topics for which you want the study guide"],
    "language": "{language of the response}"
}
"""

output_example = """
{
    "guide": [
        {
            "day": "{study day number}",
            "dayOfWeek": "{day of the week, like Monday}",
            "contents": [
                {
                    "studySubject": {
                        "subject": "{subject of study}",
                        "topic": "{topics of the subject}",
                        "description": "{description of what should be studied, including main points}",
                        "supportingMaterials": ["list of recommended materials, such as books, films, etc."],
                        "hoursOfStudy": "{study hours for this topic}"
                    }
                }
            ]
        }
    ]
}
"""
