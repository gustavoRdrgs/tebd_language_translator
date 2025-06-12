import os
from dotenv import load_dotenv
import requests

load_dotenv()

def translate_text(text, target_language):
    auth_key = os.getenv("DEEPL_API_KEY")
    url = "https://api-free.deepl.com/v2/translate"

    headers = {
        "Authorization": f"DeepL-Auth-Key {auth_key}"
    }
    params = {
        "text": text,
        "target_lang": target_language.upper()
    }
    response = requests.post(url, headers=headers, data=params)
    # Verifica se teve erro na requisição
    if response.status_code != 200:
        raise Exception(f"Erro na tradução: {response.status_code} - {response.text}")
    return response.json()["translations"][0]["text"]
