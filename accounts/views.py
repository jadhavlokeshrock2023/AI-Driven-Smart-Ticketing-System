from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


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
@login_required
def agent_dashboard(request):
    return render(request, "accounts/agent_dashboard.html")


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