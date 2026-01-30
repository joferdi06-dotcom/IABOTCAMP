import os
from groq import Groq
from dotenv import load_dotenv

# Cargar .env SOLO en local (no rompe en producción)
load_dotenv()


def generate_response(user_text, system_prompt=None):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return "❌ Error de configuración: falta la API Key de Groq."

    client = Groq(api_key=api_key)

    messages = []

    if system_prompt:
        messages.append({
            "role": "system",
            "content": system_prompt
        })

    messages.append({
        "role": "user",
        "content": user_text
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.3
    )

    return response.choices[0].message.content
