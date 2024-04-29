from typing import List
from pydantic import BaseModel

class TopicRequest(BaseModel):
    name: str
    number_of_questions: int
    difficulty: str
    multiple_choice: int
    open_ended: int

class ExerciseRequest(BaseModel):
    topics: List[TopicRequest]