"""Inicializa o cliente da API da OpenAI."""

from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Instancia o cliente da OpenAI usando a chave da API
client = OpenAI(api_key=API_KEY)