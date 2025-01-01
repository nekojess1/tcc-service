from typing import List
from pydantic import BaseModel
from api.models.common.question import Question
    
class MindMapRequest(BaseModel):
    questions: List[Question]
