from typing import List
from pydantic import BaseModel
from api.models.common.question import QuestionResponse

class Questions(BaseModel):
    title: str
    question_id: str
    responses: List[QuestionResponse]
    
class MindMapRequest(BaseModel):
    questions: List[Questions]
