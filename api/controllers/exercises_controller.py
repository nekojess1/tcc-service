from fastapi import APIRouter, HTTPException
from api.services.exercises_service import get_exercises
from api.services.exercises_validator_service import validate_exercises_strength
from api.models.requests.validade_exercises_request import ValidateExercisesRequest
from api.models.responses.validate_exercises_response import ValidationResponse
from api.models.requests.exercises_request import ExerciseRequest
from api.models.responses.exercise_response import ExercisesResponse

router = APIRouter()

@router.post('/generate/',  response_model=ExercisesResponse, status_code=200)
async def generate_exercises(request_body: ExerciseRequest):
    """Endpoint para gerar exercícios."""
    try:
        response = get_exercises(request_body)
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/validate/',  response_model=ValidationResponse, status_code=200)
async def validate_exercises(request_body: ValidateExercisesRequest):
    """Endpoint para gerar exercícios."""
    try:
        response = validate_exercises_strength(request_body)
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
