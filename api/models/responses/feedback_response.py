from pydantic import BaseModel
from typing import List

class FeedbackResponse(BaseModel):
    question_id: str
    response_id: str
    feedback: str
    type: str
    wrong_snippets: List[str]
