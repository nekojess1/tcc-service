from fastapi import FastAPI
from dotenv import load_dotenv
from api.routes.gptRoutes import router as gpt_router

#load .env
load_dotenv()

app = FastAPI()

# add routes from gptRoute.py
app.include_router(gpt_router, prefix="/api", tags=["GPT"])
