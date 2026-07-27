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

    path(
    "agent/ticket/<int:id>/",
    views.agent_ticket_detail,
    name="agent_ticket_detail"
),

path(
    "agent/ticket/<int:id>/status/",
    views.update_ticket_status,
    name="update_ticket_status"
),

path(
    "agent/ticket/<int:id>/comment/",
    views.add_ticket_comment,
    name="add_ticket_comment"
),
path(
    "customer/ticket/<int:id>/",
    views.customer_ticket_detail,
    name="customer_ticket_detail"
),
path(
    "admin/ticket/<int:id>/assign/",
    views.assign_ticket,
    name="assign_ticket"
),
]