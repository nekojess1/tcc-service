from typing import List
from pydantic import BaseModel

class MindMapRequest(BaseModel):
    subject: str
    language: str
    