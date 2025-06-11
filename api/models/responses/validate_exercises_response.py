from pydantic import BaseModel
from typing import List

class ParametersTri(BaseModel):
    parameter_a: float
    parameter_b: float
    parameter_c: float
    
class QuestionValidation(BaseModel):
    id: str
    parameters_tri: ParametersTri
    
class Students(BaseModel):
    id: str
    nivel_habilidade: float
    
class ValidationResponse(BaseModel):
    questions: List[QuestionValidation]
    students: List[Students]
