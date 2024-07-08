from fastapi import APIRouter, HTTPException
from api.services.mind_map_service import get_mind_map
from api.models.request.mind_map_request import MindMapRequest

router = APIRouter()

@router.post('/generate/mind-map/', status_code=200)
async def generate_mind_map(request_body: MindMapRequest):
    """Endpoint para gerar mind map."""
    try:
        response = get_mind_map(request_body)
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
