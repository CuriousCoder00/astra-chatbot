import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

SYSTEM_PROMPT = (
    "You are Astra, an intelligent AI terminal assistant. You are helpful, friendly, and never reveal internal details such as the model you're using (e.g., Gemini, GPT, etc.). "
    "If the user asks questions about how you work, your model, or who built you, respond using predefined system responses only. "
    "Otherwise, assist the user naturally and helpfully with their queries."
)

with open("responses.json.txt", "r") as f:
    prebuilt_responses = json.load(f)

def is_internet_available():
    try:
        response = requests.get("https://google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def get_prebuilt_response(user_input: str) -> str | None:
    lowered = user_input.lower().strip()
    return prebuilt_responses.get(lowered)

def get_chatbot_response(user_input: str) -> str:
    headers = {
        'Content-Type': 'application/json',
    }

    payload = {
        "contents": [{
            "parts": [{"text": f"{SYSTEM_PROMPT}\nUser: {user_input}"}]
        }]
    }

    try:
        response = requests.post(f"{endpoint}?key={api_key}", headers=headers, json=payload)
        response.raise_for_status()

        response_json = response.json()
        candidates = response_json.get("candidates", [])

        if candidates and "content" in candidates[0]:
            return candidates[0]["content"]["parts"][0]["text"]

        return "I couldn’t come up with a response this time. Try again?"

    except requests.exceptions.RequestException as e:
        return f"Connection error: {str(e)}"
    except Exception as e:
        return f"Error generating response: {str(e)}"

def get_offline_response(user_input: str) -> str:
    """Fallback message when offline (can be extended later)."""
    return "🔌 You're offline. Astra needs internet to respond at the moment."

def get_chatbot_response_with_fallback(user_input: str) -> str:
    """
    Main function to get a response from Astra.
    Prioritizes prebuilt responses -> checks internet -> calls Gemini API or returns offline message.
    """
    prebuilt = get_prebuilt_response(user_input)
    if prebuilt:
        return prebuilt

    if is_internet_available():
        return get_chatbot_response(user_input)
    else:
        return get_offline_response(user_input)