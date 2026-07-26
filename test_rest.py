import os
import requests
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={key}"

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Hello"
                }
            ]
        }
    ]
}

response = requests.post(url, json=data)

print("STATUS:", response.status_code)
print(response.text)