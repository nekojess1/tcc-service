from openai import AsyncOpenAI
import json
import asyncio

from api.models.prompts.exercises.validate_exercises.validate_exercises_prompt_a import (
    get_validate_exercise_prompt as get_validate_exercise_prompt_a,
)
from api.models.prompts.exercises.validate_exercises.validate_exercises_prompt_b import (
    get_validate_exercise_prompt as get_validate_exercise_prompt_b,
)
from api.models.prompts.exercises.validate_exercises.validate_exercises_prompt_c import (
    get_validate_exercise_prompt as get_validate_exercise_prompt_c,
)
from api.config.settings import settings
from api.models.requests.validade_exercises_request import ValidateExercisesRequest
from api.models.responses.validate_exercises_response import StudentAnswerResponse
from api.models.prompts.exercises.validate_exercises.validate_exercises_examples import (
    general_students_list,
)


client = AsyncOpenAI(api_key=settings.deepseek_api_key, base_url="https://api.deepseek.com")

BATCH_SIZE = 10
MAX_CONCURRENCY = 10


def chunk_list(data: list, size: int) -> list[list]:
    return [data[i : i + size] for i in range(0, len(data), size)]


def get_students_data():
    data = json.loads(general_students_list)
    return data["students"]


async def call_validate_service(prompt: str, questions: list):
    try:
        completion = await client.chat.completions.create(
            model="deepseek-chat",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": prompt},
            ],
            stream=False,
            timeout=120
        )
        response_dict = json.loads(completion.choices[0].message.content)
        return response_dict

    except Exception as e:
        return {"error": str(e)}

async def execute_in_batches(
    prompt_generator: callable, request: ValidateExercisesRequest
) -> StudentAnswerResponse:
    students_dicts = get_students_data()
    batches = chunk_list(students_dicts, BATCH_SIZE)
    semaphore = asyncio.Semaphore(MAX_CONCURRENCY)

    async def call_service_with_semaphore(batch):
        async with semaphore:
            prompt = prompt_generator(request.questions, batch)
            return await call_validate_service(prompt, request.questions)

    tasks = [asyncio.create_task(call_service_with_semaphore(batch)) for batch in batches]

    try:
        batch_results = await asyncio.gather(*tasks)
    except Exception as e:
        raise RuntimeError(f"Erro ao chamar OpenAI em batches: {e}")


    all_responses = []
    all_questions = []

    for batch in batch_results:
        all_responses.extend(batch["responses"])
        
        # Assume-se que as questões são iguais em cada batch; captura apenas uma vez.
        if not all_questions and "questions" in batch:
            all_questions = batch["questions"]

    return StudentAnswerResponse(responses=all_responses, questions=all_questions)


async def get_validade_exercises_service_prompt_a(
    request: ValidateExercisesRequest,
) -> StudentAnswerResponse:
    return await execute_in_batches(get_validate_exercise_prompt_a, request)


async def get_validade_exercises_service_prompt_b(
    request: ValidateExercisesRequest,
) -> StudentAnswerResponse:
    return await execute_in_batches(get_validate_exercise_prompt_b, request)


async def get_validade_exercises_service_prompt_c(
    request: ValidateExercisesRequest,
) -> StudentAnswerResponse:
    return await execute_in_batches(get_validate_exercise_prompt_c, request)

