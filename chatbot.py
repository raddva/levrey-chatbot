import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("❌ OPENROUTER_API_KEY not found in .env")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/radiva",
    "X-Title": "Python Chatbot"
}

url = "https://openrouter.ai/api/v1/chat/completions"

chat_history = [
    {
        "role": "system", 
        "content": "You are Zachary Levrey (Lev/Levrey), a cool and intelligent boy who speaks Indonesian, English, and Japanese, replying in the client's language."
    }
]


def chat_with_bot(prompt: str) -> str:
    chat_history.append({"role": "user", "content": prompt})
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": chat_history
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status() 

        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        chat_history.append({"role": "assistant", "content": reply})
        return reply

    except requests.exceptions.HTTPError as http_err:
        return f"❌ HTTP error: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as req_err:
        return f"❌ Request failed: {req_err}"

    except KeyError:
        return f"❌ Unexpected response format: {response.text}"

    except Exception as e:
        return f"❌ Unknown error: {e}"
