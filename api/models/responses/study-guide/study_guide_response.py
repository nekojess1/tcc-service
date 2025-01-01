from pydantic import BaseModel
from typing import List, Optional

class Question(BaseModel):
    type: str
    question: str
    answer: str
    options: Optional[List[str]] = None
    hints: Optional[List[str]] = None

class Exercise(BaseModel):
    topic: str
    questions: List[Question]

class ExercisesResponse(BaseModel):
    exercises: List[Exercise]