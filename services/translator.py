import os
import requests
from dotenv import load_dotenv

load_dotenv()

LANG_CODES = {
    "Inglês": "EN",
    "Português": "PT",
    "Espanhol": "ES",
    "Francês": "FR",
    "Alemão": "DE",
    "Italiano": "IT"
}

def translate_text(text, source_language_name, target_language_name):
    auth_key = os.getenv("DEEPL_API_KEY")
    if not auth_key:
        raise Exception("Chave da API não encontrada.")

    source_lang_code = LANG_CODES.get(source_language_name)
    target_lang_code = LANG_CODES.get(target_language_name)

    if not source_lang_code or not target_lang_code:
        raise ValueError("Idiomas não suportados.")

    url = "https://api-free.deepl.com/v2/translate"
    headers = {
        "Authorization": f"DeepL-Auth-Key {auth_key}"
    }
    params = {
        "text": text,
        "source_lang": source_lang_code,
        "target_lang": target_lang_code
    }

    response = requests.post(url, headers=headers, data=params)

    if response.status_code != 200:
        raise Exception(f"Erro na tradução: {response.status_code} - {response.text}")

    return response.json()["translations"][0]["text"]

def detect_language(text):
    auth_key = os.getenv("DEEPL_API_KEY")
    if not auth_key:
        raise Exception("Chave da API não encontrada.")

    url = "https://api-free.deepl.com/v2/translate"
    headers = {
        "Authorization": f"DeepL-Auth-Key {auth_key}"
    }
    params = {
        "text": text,
        "target_lang": "EN"
    }

    response = requests.post(url, headers=headers, data=params)

    if response.status_code != 200:
        raise Exception(f"Erro na detecção: {response.status_code} - {response.text}")

    return response.json()["translations"][0]["detected_source_language"]

