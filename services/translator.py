"""Serviços de tradução usando a API do DeepL."""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Mapeamento de nomes de idiomas para códigos da API DeepL
LANG_CODES = {
    "Inglês": "EN",
    "Português": "PT",
    "Espanhol": "ES",
    "Francês": "FR",
    "Alemão": "DE",
    "Italiano": "IT"
}

def translate_text(text, source_language_name, target_language_name):
    """
    Traduz um texto de um idioma de origem para um idioma de destino.

    Args:
        text (str): Texto a ser traduzido.
        source_language_name (str): Nome do idioma de origem (ex: "Português").
        target_language_name (str): Nome do idioma de destino (ex: "Inglês").

    Returns:
        str: Texto traduzido.

    Raises:
        Exception: Se a chave da API estiver ausente ou a requisição falhar.
        ValueError: Se os idiomas fornecidos não forem suportados.
    """
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
    """
    Detecta o idioma de origem de um texto com base na tradução automática.

    Args:
        text (str): Texto cuja língua deve ser detectada.

    Returns:
        str: Código do idioma detectado (ex: "PT", "EN").

    Raises:
        Exception: Se a chave da API estiver ausente ou a requisição falhar.
    """
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

