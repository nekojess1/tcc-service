from pydantic import BaseModel
from typing import List

class ParametersTri(BaseModel):
    parameter_a: str
    parameter_b: str
    parameter_c: str
    
class QuestionValidation(BaseModel):
    id: str
    parameters_tri: ParametersTri

class Response(BaseModel):
    student_id: str
    ability: float
    answers: List[int]

class ValidationResponse(BaseModel):
    questions: List[QuestionValidation]
    responses: List[Response]

class StudentAnswerResponse(BaseModel):
    responses: List[Response]
