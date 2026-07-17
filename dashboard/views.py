from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from tickets.models import Ticket



@login_required
def dashboard(request):

    # Total tickets created by customer

    total_tickets = Ticket.objects.filter(
        customer=request.user
    ).count()



    # Open tickets

    open_tickets = Ticket.objects.filter(
        customer=request.user,
        status="open"
    ).count()



    # Resolved tickets

    resolved_tickets = Ticket.objects.filter(
        customer=request.user,
        status="resolved"
    ).count()



    # Recent tickets

    recent_tickets = Ticket.objects.filter(
        customer=request.user
    ).order_by(
        "-created_at"
    )[:5]



    context = {

        "total_tickets": total_tickets,

        "open_tickets": open_tickets,

        "resolved_tickets": resolved_tickets,

        "recent_tickets": recent_tickets,

    }



    return render(
        request,
        "dashboard/dashboard.html",
        context
    )