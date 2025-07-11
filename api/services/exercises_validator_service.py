from openai import AsyncOpenAI
import openai
import json
from api.models.prompts.exercises.validate_exercises.validate_exercises_prompt import get_validate_exercise_prompt
from api.models.prompts.exercises.validate_exercises.validate_exercises_prompt_elementary_students import get_validate_elementary_students_exercises_prompt
from api.config.settings import settings
from api.models.requests.validade_exercises_request import ValidateExercisesRequest
from api.models.responses.validate_exercises_response import StudentAnswerResponse, ValidationResponse
from api.models.prompts.exercises.validate_exercises.validate_exercises_examples import general_students_list
import asyncio

client = AsyncOpenAI(api_key=settings.deepseek_api_key, base_url="https://api.deepseek.com")
BATCH_SIZE = 20
MAX_CONCURRENCY = 5

def validate_elementary_exercises_service(request: ValidateExercisesRequest):
    try:
        completion = openai.chat.completions.create(
            model="o4-mini",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": get_validate_elementary_students_exercises_prompt()},
                {"role": "user", "content": str(request)}
            ],
            stream=False
        )
        response_dict = json.loads(completion.choices[0].message.content)
        validated = StudentAnswerResponse(**response_dict)
        return validated
    except Exception as e:
        return {"error": str(e)}
    

def chunk_list(data: list, size: int) -> list[list]:
    return [data[i:i + size] for i in range(0, len(data), size)]


async def validate_general_exercises_service(request: ValidateExercisesRequest) -> StudentAnswerResponse:
    # 2) Fatia os estudantes
    data = json.loads(general_students_list)
    students_dicts = data["students"]

    batches = chunk_list(students_dicts, BATCH_SIZE)
    semaphore = asyncio.Semaphore(MAX_CONCURRENCY)
    async def sem_call(batch):
        async with semaphore:
            return await call_validate_general_exercises_service(request, batch)

    # 3) Dispara as tasks em paralelo (até MAX_CONCURRENCY simultâneas)
    tasks = [asyncio.create_task(sem_call(batch)) for batch in batches]
    all_responses = []
    try:
        batch_results = await asyncio.gather(*tasks)
    except Exception as e:
        raise RuntimeError(f"Erro ao chamar OpenAI em batches: {e}")

    # 4) Agrega todas as respostas num único array
    for resp_list in batch_results:
        all_responses.extend(resp_list)
    # 5) Retorna o modelo Pydantic
    return StudentAnswerResponse(responses=all_responses)
    
async def call_validate_general_exercises_service(request: ValidateExercisesRequest, students: list):
    try:
        # Sending request to OpenAI
        completion = await client.chat.completions.create(
            model="deepseek-chat",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": get_validate_exercise_prompt(len(request.questions), students)},
                {"role": "user", "content": str(request)}
            ],
            stream=False
        )
        response_dict = json.loads(completion.choices[0].message.content)
        print(response_dict)
        return response_dict["responses"]
    except Exception as e:
        return {"error": str(e)}
