from typing import List
from pydantic import BaseModel
from api.models.common.question import Question

class StoryGuideRequest(BaseModel):
    daysDuration: int
    daysOfWeek: List[str]
    hoursPerDay: float
    topics: List[str]
    language: str
