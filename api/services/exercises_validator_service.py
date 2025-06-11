from openai import OpenAI
import json
from api.models.prompts.exercises.validate_exercises.validate_exercises_prompt import get_validate_exercise_prompt
from api.models.prompts.exercises.validate_exercises.validate_exercises_prompt_elementary_students import get_validate_elementary_students_exercises_prompt
from api.config.settings import settings
from api.models.requests.validade_exercises_request import ValidateExercisesRequest
from api.models.responses.validate_exercises_response import ValidationResponse

# Initialize OpenAI client
client = OpenAI(api_key=settings.deepseek_api_key, base_url="https://api.deepseek.com")

def validate_elementary_exercises_service(request: ValidateExercisesRequest):
    """Validates exercise difficulty using OpenAI API"""
    try:
        # Sending request to OpenAI
        completion = client.chat.completions.create(
            model="deepseek-chat",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": get_validate_elementary_students_exercises_prompt()},
                {"role": "user", "content": str(request)}
            ],
            stream=False
        )
        response_dict = json.loads(completion.choices[0].message.content)
        validated = ValidationResponse(**response_dict)
        return validated
    except Exception as e:
        return {"error": str(e)}
    
def validate_general_exercises_service(request: ValidateExercisesRequest):
    """Validates exercise difficulty using OpenAI API"""
    try:
        # Sending request to OpenAI
        completion = client.chat.completions.create(
            model="deepseek-chat",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": get_validate_exercise_prompt()},
                {"role": "user", "content": str(request)}
            ],
            stream=False
        )
        response_dict = json.loads(completion.choices[0].message.content)
        validated = ValidationResponse(**response_dict)
        return validated
    except Exception as e:
        return {"error": str(e)}
