from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth import get_user_model


from .forms import TicketForm
from .models import Ticket, TicketComment


# AI Modules

from ai.predictor import (
    predict_category,
    predict_priority
)

from ai.sentiment import analyze_sentiment

from ai.similarity import find_similar_ticket

from ai.reply_generator import generate_reply



User = get_user_model()



# ==================================================
# CREATE TICKET + AI ANALYSIS
# ==================================================

@login_required
def create_ticket(request):

    similar_ticket = None


    if request.method == "POST":

        form = TicketForm(request.POST)


        if form.is_valid():

            ticket = form.save(commit=False)


            # Customer

            ticket.customer = request.user


            description = ticket.description



            # -----------------------------
            # AI Prediction
            # -----------------------------

            try:

                ticket.category = predict_category(
                    description
                )

                ticket.priority = predict_priority(
                    description
                )

                ticket.sentiment = analyze_sentiment(
                    description
                )

            except Exception as e:

                print(
                    "AI Error:",
                    e
                )



            # -----------------------------
            # Auto Assign Agent
            # -----------------------------

            agent = User.objects.filter(
                role="agent"
            ).first()


            if agent:

                ticket.assigned_agent = agent



            # -----------------------------
            # Similar Ticket Detection
            # -----------------------------

            try:

                previous_tickets = Ticket.objects.exclude(
                    id=ticket.id
                )


                similar_ticket = find_similar_ticket(
                    description,
                    previous_tickets
                )


                if similar_ticket:

                    print(
                        "Similar Ticket Found:",
                        similar_ticket["ticket"].id,
                        similar_ticket["score"]
                    )


            except Exception as e:

                print(
                    "Similarity Error:",
                    e
                )



            # Save Ticket

            ticket.save()



            return render(
                request,
                "tickets/similar_result.html",
                {
                    "ticket":ticket,
                    "similar":similar_ticket
                }
            )



    else:

        form = TicketForm()



    return render(
        request,
        "tickets/create_ticket.html",
        {
            "form":form
        }
    )





# ==================================================
# CUSTOMER MY TICKETS
# ==================================================

@login_required
def my_tickets(request):


    tickets = Ticket.objects.filter(
        customer=request.user
    ).order_by(
        "-created_at"
    )


    return render(
        request,
        "tickets/my_tickets.html",
        {
            "tickets":tickets
        }
    )





# ==================================================
# AGENT DASHBOARD
# ==================================================

# ==================================================
# AGENT DASHBOARD
# ==================================================

@login_required
def agent_tickets(request):


    # Show only tickets assigned to logged-in agent

    tickets = Ticket.objects.filter(
        assigned_agent=request.user
    )



    # =========================
    # SEARCH FILTER
    # =========================

    search = request.GET.get("search")


    if search:

        tickets = tickets.filter(
            title__icontains=search
        )



    # =========================
    # STATUS FILTER
    # =========================

    status = request.GET.get("status")


    if status:

        tickets = tickets.filter(
            status=status
        )



    # =========================
    # PRIORITY FILTER
    # =========================

    priority = request.GET.get("priority")


    if priority:

        tickets = tickets.filter(
            priority=priority
        )



    # Latest tickets first

    tickets = tickets.order_by(
        "-created_at"
    )



    return render(
        request,
        "tickets/agent_tickets.html",
        {
            "tickets": tickets
        }
    )







# ==================================================
# TICKET DETAILS
# ==================================================

@login_required
def ticket_detail(request,id):


    ticket = get_object_or_404(
        Ticket,
        id=id
    )


    comments = TicketComment.objects.filter(
        ticket=ticket
    ).order_by(
        "created_at"
    )



    return render(
        request,
        "tickets/ticket_detail.html",
        {
            "ticket":ticket,
            "comments":comments
        }
    )







# ==================================================
# ADD COMMENT
# ==================================================

@login_required
def add_comment(request,id):


    ticket = get_object_or_404(
        Ticket,
        id=id
    )


    if request.method == "POST":


        message = request.POST.get(
            "message"
        )


        if message:


            TicketComment.objects.create(

                ticket=ticket,

                user=request.user,

                message=message

            )



    return redirect(
        "ticket_detail",
        id=id
    )







# ==================================================
# UPDATE STATUS
# ==================================================

@login_required
def update_ticket_status(request,id):


    ticket = get_object_or_404(
        Ticket,
        id=id
    )


    if request.method == "POST":


        status = request.POST.get(
            "status"
        )


        ticket.status = status


        ticket.save()



    return redirect(
        "ticket_detail",
        id=id
    )








# ==================================================
# AI ANALYTICS DASHBOARD
# ==================================================

@login_required
def analytics_dashboard(request):


    total_tickets = Ticket.objects.count()



    open_tickets = Ticket.objects.filter(
        status="open"
    ).count()



    resolved_tickets = Ticket.objects.filter(
        status="resolved"
    ).count()



    priority_data = Ticket.objects.values(
        "priority"
    ).annotate(
        count=Count("priority")
    )



    sentiment_data = Ticket.objects.values(
        "sentiment"
    ).annotate(
        count=Count("sentiment")
    )



    category_data = Ticket.objects.values(
        "category"
    ).annotate(
        count=Count("category")
    )



    return render(
        request,
        "tickets/analytics.html",
        {

            "total_tickets":total_tickets,

            "open_tickets":open_tickets,

            "resolved_tickets":resolved_tickets,

            "priority_data":priority_data,

            "sentiment_data":sentiment_data,

            "category_data":category_data

        }
    )







# ==================================================
# AI GENERATED REPLY
# ==================================================

@login_required
def ai_reply(request,id):


    ticket = get_object_or_404(
        Ticket,
        id=id
    )


    try:

        reply = generate_reply(
            ticket.description
        )

    except Exception:

        reply = (
            "AI reply service unavailable."
        )



    return render(
        request,
        "tickets/ai_reply.html",
        {
            "ticket":ticket,
            "reply":reply
        }
    )
from django.shortcuts import render

def ticket_home(request):
    return render(request, "home.html")