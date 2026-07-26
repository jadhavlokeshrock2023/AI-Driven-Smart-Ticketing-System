from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

print("KEY START:", key[:10])
print("KEY LENGTH:", len(key))

client = genai.Client(
    api_key=key
)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Hello"
)

print(response.text)