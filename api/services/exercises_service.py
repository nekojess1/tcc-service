import openai
import json
from api.models.prompts.exercises.exercises_prompt import get_exercise_prompt
from api.models.requests.exercises_request import ExerciseRequest

def get_exercises(exercise_request: ExerciseRequest):
    """Generates personalized study guide using OpenAI gpt-4-0125-preview"""
    completion = openai.chat.completions.create(
        model="gpt-4o",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": get_exercise_prompt()},
            {"role": "user", "content": str(exercise_request)}
        ]
    )
    response = json.loads(completion.choices[0].message.content)
    return response