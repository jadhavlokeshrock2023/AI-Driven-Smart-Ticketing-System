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

            # Automatically login after registration
            login(request, user)

            return redirect("dashboard")

    else:

        form = RegisterForm()


    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )



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
            password=password
        )


        if user is not None:

            login(request, user)

            return redirect("dashboard")


        else:

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



# ==========================
# User Logout
# ==========================

def logout_view(request):

    logout(request)

    return redirect("login")



# ==========================
# Dashboard
# ==========================

@login_required
def dashboard(request):

    user = request.user

    if user.role == "customer":
        return render(
            request,
            "accounts/customer_dashboard.html"
        )

    elif user.role == "agent":
        return render(
            request,
            "accounts/agent_dashboard.html"
        )

    elif user.role == "admin":
        return render(
            request,
            "accounts/admin_dashboard.html"
        )

    else:
        return render(
            request,
            "accounts/dashboard.html"
        )