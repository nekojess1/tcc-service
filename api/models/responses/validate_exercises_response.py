from pydantic import BaseModel
from typing import List

class Response(BaseModel):
    student_id: str
    ability: float
    selected_options: List[str] = None
    answers: List[int]

class Questions(BaseModel):
    id: str
    difficulty: float
    correct_rate: float

class StudentAnswerResponse(BaseModel):
    responses: List[Response]
    questions: List[Questions] = None
