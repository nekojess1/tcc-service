from pydantic import BaseModel
from typing import List, Optional

class Question(BaseModel):
    type: str
    question: str
    options: Optional[List[str]] = None  
    answer: str

class ExercisesResponse(BaseModel):
    topic: str
    questions: List[Question]