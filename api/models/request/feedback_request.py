from typing import List
from pydantic import BaseModel

class QuestionResponse(BaseModel):
    answer: str
    response_id: str
    email: str
    form_id: str
      
class Question(BaseModel):
    title: str
    question_id: str
    response: QuestionResponse


class FeedbackRequest(BaseModel):
    question: Question
    feedbackList: List[str]
