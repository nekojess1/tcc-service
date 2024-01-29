from fastapi import FastAPI
from api.routes.generateFeedback import get_feedback
from dotenv import load_dotenv
from api.models.request.FeedbackRequest import FeedbackRequest


#load Env
load_dotenv()

app = FastAPI()

@app.post('/generate-feedback/', status_code=200)
async def generate_feedback(requestBody: FeedbackRequest):
    return  get_feedback(requestBody.userContent, requestBody.feedbacks)

