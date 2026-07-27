# ==========================================
# AI Reply Generator
# ==========================================

from ai.groq import ask_groq



# ==========================================
# Generate AI Customer Support Reply
# ==========================================


def generate_reply(ticket_description):


    prompt = f"""

You are an expert AI Customer Support Agent
working for an AI Smart Ticketing System.


Generate a professional reply for the
customer support ticket below.


Customer Issue:

{ticket_description}



Instructions:

1. Start with a polite greeting.

2. Acknowledge the customer's problem.

3. Provide simple troubleshooting steps.

4. Explain what the support team will do.

5. Keep the response short and professional.

6. Avoid complicated technical words.

7. Ask for more details if required.

8. End with a professional closing.


Generate ONLY the customer reply.
Do not add explanations.

"""



    try:


        reply = ask_groq(
            prompt
        )



        # Check empty response

        if reply and reply.strip():

            return reply



        else:

            return fallback_reply()



    except Exception as e:


        print(
             "Groq Reply Error:",
            e
        )


        return fallback_reply()





# ==========================================
# Default Reply When AI Fails
# ==========================================


def fallback_reply():


    return """

Hello,

Thank you for contacting our support team.

We have received your request and our team
is currently analyzing your issue.

Our support executive will contact you soon
with the appropriate solution.

Thank you for your patience.

Regards,

AI Smart Ticketing Support Team

"""