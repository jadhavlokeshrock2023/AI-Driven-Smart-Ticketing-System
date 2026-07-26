from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_groq(message):

    try:

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "system",
                    "content": 
                    "You are an AI customer support assistant."
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

        return "AI service temporarily unavailable."