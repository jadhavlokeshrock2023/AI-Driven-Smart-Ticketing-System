import google.generativeai as genai
import os


API_KEY = os.getenv("GEMINI_API_KEY")


genai.configure(
    api_key=API_KEY
)


model = genai.GenerativeModel(
    "gemini-1.5-flash"
)



def ask_gemini(message):

    try:

        response = model.generate_content(
            message
        )

        return response.text


    except Exception as e:

        print(e)

        return (
            "Sorry, AI service is temporarily unavailable."
        )