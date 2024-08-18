from pydantic import BaseModel

class QuestionResponse(BaseModel):
    answer: str
    response_id: str
    type: str = ""

class Question(BaseModel):
    title: str
    question_id: str
    response: QuestionResponse
