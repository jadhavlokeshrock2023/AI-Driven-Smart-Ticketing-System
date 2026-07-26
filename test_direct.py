import os
from dotenv import load_dotenv
from google import genai

load_dotenv(override=True)

key = os.getenv("GEMINI_API_KEY")

print("KEY EXISTS:", key is not None)
print("KEY START:", key[:10])
print("KEY LENGTH:", len(key))

client = genai.Client(
    api_key=key
)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Say hello"
)

print(response.text)