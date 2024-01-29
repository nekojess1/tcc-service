from pydantic import BaseModel

class QuestionResponse(BaseModel):
    answer: str
    response_id: str
    feedback: str
    email: str
    form_id: str
    type: str

class FeedbackResponse(BaseModel):
    title: str
    question_id: str
    response: QuestionResponse
