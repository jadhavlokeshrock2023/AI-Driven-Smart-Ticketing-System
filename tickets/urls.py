from django.urls import path
from . import views


urlpatterns = [

    path(
        "create/",
        views.create_ticket,
        name="create_ticket"
    ),

    path(
    "my-tickets/",
    views.my_tickets,
    name="my_tickets"),

    path(
    "agent/",
    views.agent_tickets,
    name="agent_tickets"),

     path(
        "<int:id>/",
        views.ticket_detail,
        name="ticket_detail"
    ),
    path(
    "<int:id>/update-status/",
    views.update_ticket_status,
    name="update_ticket_status"),    

    path(
    "analytics/",
    views.analytics_dashboard,
    name="analytics"),

    path(
    "<int:id>/comment/",
    views.add_comment,
    name="add_comment"),
   
    path(
    "<int:id>/ai-reply/",
    views.ai_reply,
    name="ai_reply"),

]