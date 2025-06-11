from pydantic import BaseModel
from typing import List, Optional

class Question(BaseModel):
    type: str
    question: str
    options: Optional[List[str]] = None  # Opcional, pois nem todos os tipos de perguntas têm opções
    answer: str

class Exercise(BaseModel):
    topic: str
    questions: List[Question]

class ExercisesResponse(BaseModel):
    exercises: List[Exercise]
