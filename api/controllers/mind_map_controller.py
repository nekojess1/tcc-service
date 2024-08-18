from fastapi import APIRouter, HTTPException
from api.services.mind_map_service import get_mind_map, get_mind_map_old
from api.models.requests.mind_map_request import MindMapRequest
from api.models.requests.mind_map_request_old import MindMapRequest as MindMapRequestOld

router = APIRouter()

@router.post('/generate/', status_code=200)
async def generate_mind_map(request_body: MindMapRequest):
    """Endpoint para gerar mind map."""
    try:
        response = get_mind_map(request_body)
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/generate/old', status_code=200)
async def generate_mind_map(request_body: MindMapRequestOld):
    """Endpoint para gerar mind map."""
    try:
        response = get_mind_map_old(request_body)
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
