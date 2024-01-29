from fastapi import APIRouter
from api.services.gpt_services import get_feedback
from api.models.request.feedback_request import FeedbackRequest

router = APIRouter()

@router.post('/generate-feedback/', status_code=200)
async def generate_feedback(requestBody: FeedbackRequest):
    return get_feedback(requestBody.userContent, requestBody.feedbacks)