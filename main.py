from fastapi import FastAPI
from api.routes.generateFeedback import get_feedback
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel
from api.models.request import FeedbackRequest


class Teste(BaseModel):
  #  userContent: FeedbackRequest  <<<< ajustar depois, dando erro
    userContent: str
    feedbacks: List[str] 


#load Env
load_dotenv()

app = FastAPI()

@app.post('/generate-feedback', status_code=200)
async def generate_feedback(requestBody: Teste):
    return  get_feedback(requestBody.userContent, requestBody.feedbacks)

