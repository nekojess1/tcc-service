from pydantic import BaseModel
from typing import List

class QuestionValidation(BaseModel):
    title: str
    level: int
    motive: str

class ValidationResponse(BaseModel):
    questions: List[QuestionValidation]
    hard_questions_quantity: int
    medium_questions_quantity: int
    easy_questions_quantity: int
    average_difficulty: float
