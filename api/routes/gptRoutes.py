from fastapi import APIRouter
from api.services.gptServices import get_feedback
from api.models.request.FeedbackRequest import FeedbackRequest

router = APIRouter()

@router.post('/generate-feedback/', status_code=200)
async def generate_feedback(requestBody: FeedbackRequest):
    return get_feedback(requestBody.userContent, requestBody.feedbacks)