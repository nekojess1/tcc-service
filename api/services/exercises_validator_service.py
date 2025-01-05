# Install the OpenAI SDK first: `pip install openai`

from openai import OpenAI
import json
from api.models.prompts.exercises.validate_exercises_prompt import get_validate_exercise_prompt
from api.config.settings import settings
from api.models.responses.exercise_response import ExercisesResponse

# Initialize OpenAI client
client = OpenAI(api_key=settings.deepseek_api_key, base_url="https://api.deepseek.com")

def validate_exercises_strength(request: ExercisesResponse):
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
        
        # Parsing the response
        response = json.loads(completion.choices[0].message.content)
        return response
    except Exception as e:
        return {"error": str(e)}
