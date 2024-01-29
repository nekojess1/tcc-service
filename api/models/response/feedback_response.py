from pydantic import BaseModel

class ResponseContent(BaseModel):
    answer: str
    response_id: str
    feedback: str
    email: str
    form_id: str
    type: str

class FeedbackResponse(BaseModel):
    title: str
    question_id: str
    response: ResponseContent


