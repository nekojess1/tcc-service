from typing import List, Optional
from pydantic import BaseModel


class Exercises(BaseModel):
    id: str
    question: str
    options: Optional[List[str]] = None 

class ValidateExercisesRequest(BaseModel):
    questions: List[Exercises]
