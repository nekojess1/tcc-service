from fastapi import APIRouter, HTTPException
from api.services.exercises_service import generate_exercises_service
from api.services.exercises_validator_service import (
    validate_elementary_exercises_service,
    validate_general_exercises_service
)
from api.models.requests.exercises_request import ExerciseRequest
from api.models.responses.exercise_response import ExercisesResponse
from api.models.responses.validate_exercises_response import StudentAnswerResponse
from api.models.requests.validade_exercises_request import ValidateExercisesRequest
import time

router = APIRouter()

@router.post('/generate/', response_model=ExercisesResponse, status_code=200)
async def generate_exercises(request_body: ExerciseRequest):
    """Endpoint para gerar exercícios."""
    try:
        response = generate_exercises_service(request_body)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/generate/students-answers-prompt-a', response_model=StudentAnswerResponse, status_code=200)
async def generate_students_answers_prompt_a(request_body: ValidateExercisesRequest):
    """Endpoint para simular a resposta de estudantes para determinadas questões usando o prompt a."""
    try:
        start_time = time.perf_counter()
        response = await validate_general_exercises_service(request_body)
        elapsed = time.perf_counter() - start_time
        print(f"{elapsed:.4f}")
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/generate/students-answers-prompt-b', response_model=StudentAnswerResponse, status_code=200)
async def generate_students_answers_prompt_b(request_body: ValidateExercisesRequest):
    """Endpoint para simular a resposta de estudantes para determinadas questões usando o prompt b."""
    try:
        start_time = time.perf_counter()
        response = validate_elementary_exercises_service(request_body)
        elapsed = time.perf_counter() - start_time
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/generate/students-answers-prompt-c', response_model=StudentAnswerResponse, status_code=200)
async def generate_students_answers_prompt_c(request_body: ValidateExercisesRequest):
    """Endpoint para simular a resposta de estudantes para determinadas questões usando o prompt c."""
    try:
        start_time = time.perf_counter()
        response = validate_elementary_exercises_service(request_body)
        elapsed = time.perf_counter() - start_time
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
