from pydantic import BaseModel
from typing import List

class FeedbackResponseContent(BaseModel):
    answer: str
    response_id: str
    email: str
    form_id: str
      
class Feedback(BaseModel):
    title: str
    question_id: str
    response: FeedbackResponseContent


class FeedbackRequest(BaseModel):
    userContent: Feedback
    feedbacks: List[str] 

