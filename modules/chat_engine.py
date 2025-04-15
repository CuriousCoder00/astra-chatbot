import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def is_internet_available():
    try:
        response = requests.get("https://google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False


def get_chatbot_response(user_input: str) -> str:
    headers = {
        'Content-Type': 'application/json',
    }

    payload = {
        "contents": [{
            "parts": [{"text": user_input}]
        }]
    }

    try:
        response = requests.post(f"{endpoint}?key={api_key}", headers=headers, json=payload)

        if response.status_code == 200:
            response_json = response.json()
            candidates = response_json.get("candidates", [])
            if candidates and "content" in candidates[0]:
                return candidates[0]["content"]["parts"][0]["text"]
            else:
                return "No response content found."
        else:
            return f"Error {response.status_code}: {response.text}"

    except Exception as e:
        return f"Error generating response: {str(e)}"

def get_offline_response(user_input: str) -> str:
    # Placeholder for offline response logic
    return "Offline mode is not supported yet."

def get_chatbot_response_with_fallback(user_input: str) -> str:
    if is_internet_available():
        return get_chatbot_response(user_input)
    else:
        return "Internet connection is not available. Please check your connection."