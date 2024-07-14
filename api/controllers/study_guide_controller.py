from fastapi import APIRouter, HTTPException
from api.services.study_guide_service import get_study_guide
from api.models.request.study_guide_request import StudyGuideRequest

router = APIRouter()

@router.post('/generate/', status_code=200)
async def generate_study_guide(request_body: StudyGuideRequest):
    """Endpoint para gerar guia de estudo."""
    try:
        response = get_study_guide(request_body)
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
