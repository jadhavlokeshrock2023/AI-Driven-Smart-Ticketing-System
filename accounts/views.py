from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .forms import RegisterForm
from tickets.models import Ticket, TicketComment


User = get_user_model()


# =========================
# REGISTER
# =========================

def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            if user.role == "admin":
                return redirect("admin_dashboard")

            elif user.role == "agent":
                return redirect("agent_dashboard")

            elif user.role == "customer":
                return redirect("customer_dashboard")

            else:
                return redirect("dashboard")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


# =========================
# LOGIN
# =========================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.role == "admin":

                return redirect("admin_dashboard")

            elif user.role == "agent":

                return redirect("agent_dashboard")

            elif user.role == "customer":

                return redirect("customer_dashboard")

            else:

                return redirect("dashboard")

        return render(
            request,
            "accounts/login.html",
            {
                "error": "Invalid username or password"
            }
        )

    return render(
        request,
        "accounts/login.html"
    )


# =========================
# LOGOUT
# =========================

def logout_view(request):

    logout(request)

    return redirect("login")


# =========================
# CUSTOMER DASHBOARD
# =========================

@login_required
def customer_dashboard(request):

    tickets = Ticket.objects.filter(
        customer=request.user
    ).order_by("-created_at")

    total_tickets = tickets.count()

    open_tickets = tickets.filter(
        status="open"
    ).count()

    resolved_tickets = tickets.filter(
        status="resolved"
    ).count()

    recent_tickets = tickets[:5]

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "tickets": tickets,
            "recent_tickets": recent_tickets,
            "total_tickets": total_tickets,
            "open_tickets": open_tickets,
            "resolved_tickets": resolved_tickets,
        }
    )


# =========================
# AGENT DASHBOARD
# =========================

@login_required
def agent_dashboard(request):

    tickets = Ticket.objects.filter(
        assigned_agent=request.user
    ).order_by("-created_at")

    return render(
        request,
        "accounts/agent_dashboard.html",
        {
            "tickets": tickets
        }
    )


# =========================
# ADMIN DASHBOARD
# =========================

@login_required
def admin_dashboard(request):

    return render(
        request,
        "accounts/admin_dashboard.html"
    )


# =========================
# GENERAL DASHBOARD
# =========================

@login_required
def dashboard(request):

    if request.user.role == "admin":

        return redirect("admin_dashboard")

    elif request.user.role == "agent":

        return redirect("agent_dashboard")

    elif request.user.role == "customer":

        return redirect("customer_dashboard")

    return redirect("login")


# =========================
# AGENT TICKET DETAIL
# =========================

@login_required
def agent_ticket_detail(request, id):

    ticket = get_object_or_404(
        Ticket,
        id=id
    )

    comments = TicketComment.objects.filter(
        ticket=ticket
    ).order_by("created_at")

    return render(
        request,
        "accounts/agent_ticket_detail.html",
        {
            "ticket": ticket,
            "comments": comments
        }
    )


# =========================
# UPDATE TICKET STATUS
# =========================

@login_required
def update_ticket_status(request, id):

    ticket = get_object_or_404(
        Ticket,
        id=id
    )

    if request.method == "POST":

        status = request.POST.get("status")

        ticket.status = status

        ticket.save()

    return redirect(
        "agent_ticket_detail",
        id=id
    )


# =========================
# ADD TICKET COMMENT
# =========================

@login_required
def add_ticket_comment(request, id):

    ticket = get_object_or_404(
        Ticket,
        id=id
    )

    if request.method == "POST":

        message = request.POST.get("message")

        if message:

            TicketComment.objects.create(
                ticket=ticket,
                user=request.user,
                message=message
            )

    return redirect(
        "agent_ticket_detail",
        id=id
    )


# =========================
# CUSTOMER TICKET DETAIL
# =========================

@login_required
def customer_ticket_detail(request, id):

    ticket = get_object_or_404(
        Ticket,
        id=id,
        customer=request.user
    )

    comments = TicketComment.objects.filter(
        ticket=ticket
    ).order_by("created_at")

    return render(
        request,
        "accounts/customer_ticket_detail.html",
        {
            "ticket": ticket,
            "comments": comments
        }
    )


# =========================
# ASSIGN TICKET
# =========================

@login_required
def assign_ticket(request, id):

    ticket = get_object_or_404(
        Ticket,
        id=id
    )

    agents = User.objects.filter(
        role="agent"
    )

    if request.method == "POST":

        agent_id = request.POST.get("agent")

        agent = get_object_or_404(
            User,
            id=agent_id,
            role="agent"
        )

        ticket.assigned_agent = agent

        ticket.save()

        return redirect(
            "admin_dashboard"
        )

    return render(
        request,
        "accounts/assign_ticket.html",
        {
            "ticket": ticket,
            "agents": agents
        }
    )