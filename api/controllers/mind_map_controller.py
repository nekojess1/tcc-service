from fastapi import APIRouter, HTTPException
from api.services.mind_map_service import get_mind_map
from api.models.requests.mind_map_request import MindMapRequest
from api.models.requests.mind_map_request_old import MindMapRequest as MindMapRequestOld

router = APIRouter()

@router.post('/generate/', status_code=200)
async def generate_mind_map(request_body: MindMapRequest):
    try:
        response = get_mind_map(request_body)
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

