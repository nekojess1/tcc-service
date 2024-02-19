from typing import List
from pydantic import BaseModel
from api.models.common.question import Question

class StudyGuideRequest(BaseModel):
    daysDuration: int
    daysOfWeek: List[str]
    hoursPerDay: float
    topics: List[str]
    language: str
