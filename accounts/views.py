from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from tickets.models import Ticket, TicketComment


# ==========================
# User Registration
# ==========================
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            # Redirect based on role
            if user.role == "admin":
                return redirect("admin_dashboard")
            elif user.role == "agent":
                return redirect("agent_dashboard")
            else:
                return redirect("customer_dashboard")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


# ==========================
# User Login
# ==========================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)

            # Redirect based on role
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
            {"error": "Invalid username or password"},
        )

    return render(request, "accounts/login.html")


# ==========================
# Logout
# ==========================
def logout_view(request):
    logout(request)
    return redirect("login")


# ==========================
# Customer Dashboard
# ==========================
@login_required
def customer_dashboard(request):
    return render(request, "accounts/customer_dashboard.html")


# ==========================
# Agent Dashboard
# ==========================
from tickets.models import Ticket


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

# ==========================
# Admin Dashboard
# ==========================
@login_required
def admin_dashboard(request):
    return render(request, "accounts/admin_dashboard.html")


# ==========================
# Common Dashboard
# ==========================
@login_required
def dashboard(request):
    if request.user.role == "admin":
        return redirect("admin_dashboard")

    elif request.user.role == "agent":
        return redirect("agent_dashboard")

    elif request.user.role == "customer":
        return redirect("customer_dashboard")

    return render(request, "accounts/dashboard.html")

# ==========================
# Agent Ticket Detail
# ==========================

@login_required
def agent_ticket_detail(request, id):

    ticket = Ticket.objects.get(id=id)

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



# ==========================
# Update Ticket Status
# ==========================

@login_required
def update_ticket_status(request, id):

    ticket = Ticket.objects.get(id=id)


    if request.method == "POST":

        status = request.POST.get("status")

        ticket.status = status
        ticket.save()


    return redirect(
        "agent_ticket_detail",
        id=id
    )



# ==========================
# Add Comment
# ==========================

@login_required
def add_ticket_comment(request, id):

    ticket = Ticket.objects.get(id=id)


    if request.method == "POST":

        message = request.POST.get("message")


        TicketComment.objects.create(
            ticket=ticket,
            user=request.user,
            message=message
        )


    return redirect(
        "agent_ticket_detail",
        id=id
    )