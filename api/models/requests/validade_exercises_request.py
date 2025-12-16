from typing import List, Optional
from pydantic import BaseModel

class ParametersTri(BaseModel):
    parameter_a: str
    parameter_b: str
    parameter_c: str
    
class Exercises(BaseModel):
    id: str
    question: str
    options: Optional[List[str]] = None
    parameters: ParametersTri = None

class ValidateExercisesRequest(BaseModel):
    questions: List[Exercises]
