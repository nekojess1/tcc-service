from fastapi import FastAPI
from dotenv import load_dotenv
from api.routes.gpt_routes import router as gpt_router
import openai
from api.config.settings import settings

# Carregar variáveis de ambiente
load_dotenv()

# Configurar a chave da API OpenAI 
openai.api_key = settings.openai_api_key

app = FastAPI()

# Incluir rotas do gpt_routes
app.include_router(gpt_router)
