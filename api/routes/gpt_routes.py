from fastapi import APIRouter
from api.services.gpt_services import get_feedback, get_mind_map, get_study_guide
from api.models.request.feedback_request import FeedbackRequest
from api.models.request.mind_map_request import MindMapRequest
from api.models.request.study_guide_request import StudyGuideRequest

router = APIRouter()

@router.post('/generate/feedback/', status_code=200)
async def generate_feedback(request_body: FeedbackRequest):
    """Endpoint for generating personalized feedback."""
    return get_feedback(request_body.question, request_body.feedbackList)

@router.post('/generate/mind-map/', status_code=200)
async def generate_mind_map(request_body: MindMapRequest):
    """Endpoint for generating mind map."""
    return get_mind_map(request_body.questions)

@router.post('/generate/study-guide/', status_code=200)
async def generate_study_guide(request_body: StudyGuideRequest):
    """Endpoint for generating study guide."""
    return get_study_guide(request_body)
