from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import ChatConversation

from tickets.models import Ticket

from ai.knowledge_search import search_solution

from ai.predictor import (
    predict_category,
    predict_priority,
)

from ai.sentiment import analyze_sentiment

from .groq_ai import ask_groq



User = get_user_model()



# =====================================
# AI Chatbot Page
# =====================================

@login_required
def chatbot_page(request):

    response = ""


    if request.method == "POST":

        message = request.POST.get(
            "message",
            ""
        ).strip()


        if message:


            # =====================================
            # Step 1: Knowledge Base Search
            # =====================================

            knowledge_result = search_solution(
                message
            )


            if knowledge_result:


                response = f"""
🧠 Knowledge Base Solution Found

📌 Problem:
{knowledge_result['title']}


✅ Solution:

{knowledge_result['solution']}


If your issue is not solved, I can create a support ticket.
"""


            else:


                # =====================================
                # Step 2: Groq AI Response
                # =====================================

                ai_reply = ask_groq(
                    message
                )



                # =====================================
                # Step 3: AI Analysis
                # =====================================

                category = predict_category(
                    message
                )


                priority = predict_priority(
                    message
                )


                sentiment = analyze_sentiment(
                    message
                )



                # =====================================
                # Step 4: Find Support Agent
                # =====================================

                agent = User.objects.filter(
                    role="agent"
                ).first()



                # =====================================
                # Step 5: Create Ticket
                # =====================================

                ticket = Ticket.objects.create(

                    customer=request.user,

                    assigned_agent=agent,

                    title=message[:100],

                    description=message,

                    category=category,

                    priority=priority,

                    sentiment=sentiment,

                    status="open"

                )



                # =====================================
                # Final AI Response
                # =====================================

                response = f"""
🤖 AI Customer Support Assistant


{ai_reply}


━━━━━━━━━━━━━━━━━━


🎫 Ticket Created Successfully


🆔 Ticket ID:
#{ticket.id}


📂 Category:
{category}


⚠ Priority:
{priority}


😊 Sentiment:
{sentiment}


Our support team will contact you soon.
"""



            # =====================================
            # Save Conversation
            # =====================================

            ChatConversation.objects.create(

                user=request.user,

                message=message,

                response=response

            )



    # =====================================
    # Load Chat History
    # =====================================

    chats = ChatConversation.objects.filter(

        user=request.user

    ).order_by(
        "-created_at"
    )



    return render(

        request,

        "chatbot/chatbot.html",

        {
            "response": response,

            "chats": chats
        }

    )