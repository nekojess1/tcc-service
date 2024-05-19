from typing import List
from pydantic import BaseModel

class StudyGuideRequest(BaseModel):
    daysDuration: int
    daysOfWeek: List[str]
    hoursPerDay: str
    topics: List[str]
    language: str
