from fastapi import APIRouter, HTTPException
from api.services.exercises_service import generate_exercises_service
from api.services.exercises_validator_service import (
    validate_elementary_exercises_service,
    validate_general_exercises_service
)
from api.models.requests.exercises_request import ExerciseRequest
from api.models.responses.exercise_response import ExercisesResponse
from api.models.responses.validate_exercises_response import ValidationResponse
from api.models.requests.validade_exercises_request import ValidateExercisesRequest

router = APIRouter()

@router.post('/generate/', response_model=ExercisesResponse, status_code=200)
async def generate_exercises(request_body: ExerciseRequest):
    """Endpoint para gerar exercícios."""
    try:
        response = generate_exercises_service(request_body)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/validate/elementary-students', response_model=ValidationResponse, status_code=200)
async def validate_elementary_exercises(request_body: ValidateExercisesRequest):
    """Endpoint para validar exercícios com estudantes do ensino fundamental."""
    try:
        response = validate_elementary_exercises_service(request_body)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/validate/general-students', response_model=ValidationResponse, status_code=200)
async def validate_general_exercises(request_body: ValidateExercisesRequest):
    """Endpoint para validar exercícios gerais para estudantes (ex.: ensino médio)."""
    try:
        response = validate_general_exercises_service(request_body)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
