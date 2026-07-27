from django.urls import path
from . import views

urlpatterns = [
    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "customer/",
        views.customer_dashboard,
        name="customer_dashboard"
    ),

    path(
        "agent/",
        views.agent_dashboard,
        name="agent_dashboard"
    ),

    path(
        "admin-dashboard/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),
]