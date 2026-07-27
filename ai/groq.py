from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")


if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing")


client = Groq(
    api_key=GROQ_API_KEY
)



def ask_groq(message):

    try:

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "system",
                    "content": "You are an expert AI customer support assistant."
                },
                {
                    "role": "user",
                    "content": message
                }
            ],

            temperature=0.7
        )


        return response.choices[0].message.content


    except Exception as e:

        print("Groq Error:", e)

        return None