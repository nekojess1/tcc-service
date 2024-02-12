from typing import List
from pydantic import BaseModel
from api.models.common.question import Question

class FeedbackRequest(BaseModel):
    question: Question
    feedbackList: List[str]
