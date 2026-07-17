from django.contrib import admin

from .models import Ticket, TicketComment



@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):

    list_display = (

        "title",

        "customer",

        "assigned_agent",

        "category",

        "priority",

        "sentiment",

        "status",

        "created_at",

    )


    list_filter = (

        "category",

        "priority",

        "status",

        "sentiment",

    )


    search_fields = (

        "title",

        "description",

        "customer__username",

    )





@admin.register(TicketComment)
class TicketCommentAdmin(admin.ModelAdmin):

    list_display = (

        "ticket",

        "user",

        "message",

        "created_at",

    )


    search_fields = (

        "ticket__title",

        "user__username",

        "message",

    )