# ==========================================
# Groq AI Customer Support Assistant
# ==========================================

from groq import Groq
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()


# Get Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


if not GROQ_API_KEY:
    raise Exception("GROQ_API_KEY is missing")


# Initialize Groq Client
client = Groq(
    api_key=GROQ_API_KEY
)


# ==========================================
# Generate AI Response
# ==========================================

def ask_groq(message):

    try:

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[

                {
                    "role": "system",
                    "content": """
You are an AI customer support assistant
for an AI Smart Ticketing System.

Your job is to generate helpful,
professional and simple customer support replies.

Rules:
- Be polite
- Understand the customer's issue
- Give clear solutions
- Avoid complicated technical terms
- Keep responses short and professional
"""
                },

                {
                    "role": "user",
                    "content": message
                }

            ],

            temperature=0.7,

            max_tokens=500

        )


        return response.choices[0].message.content.strip()


    except Exception as e:

        print("Groq API Error:", e)

        return """
Hello,

Thank you for contacting our support team.

We have received your request and our team
is currently working on your issue.

We will get back to you soon with a solution.

Regards,
AI Smart Ticketing Support Team
"""