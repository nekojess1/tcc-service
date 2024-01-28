from pydantic import BaseModel, BaseConfig

class ResponseContent(BaseModel):
    answer: str
    response_id: str
    email: str
    form_id: str
      

class FeedbackRequest(BaseModel):
    title: str
    question_id: str
    response: ResponseContent

