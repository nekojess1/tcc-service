from typing import List, Optional
from pydantic import BaseModel


class Exercises(BaseModel):
    title: str
    choices: Optional[List[str]] = None 
class ValidateExercisesRequest(BaseModel):
    questions: List[Exercises]