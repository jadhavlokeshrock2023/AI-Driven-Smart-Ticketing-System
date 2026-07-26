from chatbot.groq_ai import ask_groq


response = ask_groq(
    "My internet connection is not working"
)


print("\nAI RESPONSE:")
print(response)