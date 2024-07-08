# controllers/study_guide_controller.py
from fastapi import APIRouter
from api.services.gpt_services import get_study_guide
from api.models.request.study_guide_request import StudyGuideRequest

router = APIRouter()

@router.post('/generate/study-guide/', status_code=200)
async def generate_study_guide(request_body: StudyGuideRequest):
    """Endpoint para gerar guia de estudo."""
    try:
        response = get_study_guide(request_body)
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
