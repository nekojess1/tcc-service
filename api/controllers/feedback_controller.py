from fastapi import APIRouter, HTTPException
from api.services.feedback_service import get_feedback
from api.models.requests.feedback_request import FeedbackRequest
from api.models.responses.feedback_response import FeedbackResponse

router = APIRouter()

@router.post('/generate/', response_model=FeedbackResponse, status_code=200)
async def generate_feedback(request_body: FeedbackRequest):
    """Endpoint para gerar feedback personalizado."""
    try:
        feedback_list = request_body.feedbackList
        question = request_body.question

        if not question:
            raise HTTPException(status_code=400, detail="Question and feedback list are required.")

        response = get_feedback(question, feedback_list)
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
