from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),


    # Accounts
    path(
        "accounts/",
        include("accounts.urls")
    ),


    # Tickets
    path(
        "tickets/",
        include("tickets.urls")
    ),


    # Chatbot
    path(
        "chatbot/",
        include("chatbot.urls")
    ),


    # Dashboard
    path(
        "dashboard/",
        include("dashboard.urls")
    ),


    # Home
    path(
        "",
        include("dashboard.urls")
    ),

]