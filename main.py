from fastapi import FastAPI
from dotenv import load_dotenv
from api.routes.gpt_routes import router as gpt_router

# Carregar variáveis de ambiente
load_dotenv()

app = FastAPI()

# Incluir rotas do gpt_routes
app.include_router(gpt_router)
