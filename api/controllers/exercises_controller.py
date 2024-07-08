# controllers/exercises_controller.py
from fastapi import APIRouter
from api.services.gpt_services import get_exercises
from api.models.request.exercises_request import ExerciseRequest

router = APIRouter()

@router.post('/generate/exercises/', status_code=200)
async def generate_exercises(request_body: ExerciseRequest):
    """Endpoint para gerar exercícios."""
    try:
        response = get_exercises(request_body)
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
