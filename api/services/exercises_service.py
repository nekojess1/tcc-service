import openai
import json
from api.models.prompts.exercises.generate_exercises.exercises_prompt import get_exercise_prompt
from api.models.requests.exercises_request import ExerciseRequest

def generate_exercises_service(exercise_request: ExerciseRequest):
    """Generates personalized exercises using OpenAI gpt-4-0125-preview"""
    completion = openai.chat.completions.create(
        model="o4-mini",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": get_exercise_prompt(exercise_request)},
            {"role": "user", "content": str(exercise_request.topic)}
        ]
    )
    response = json.loads(completion.choices[0].message.content)
    return response