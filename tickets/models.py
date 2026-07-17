from django.db import models
from django.conf import settings



# ==========================
# Ticket Model
# ==========================

class Ticket(models.Model):


    CATEGORY_CHOICES = (

        ('technical', 'Technical Issue'),

        ('billing', 'Billing'),

        ('general', 'General'),

        ('other', 'Other'),

    )


    PRIORITY_CHOICES = (

        ('low', 'Low'),

        ('medium', 'Medium'),

        ('high', 'High'),

        ('urgent', 'Urgent'),

    )


    STATUS_CHOICES = (

        ('open', 'Open'),

        ('progress', 'In Progress'),

        ('resolved', 'Resolved'),

        ('closed', 'Closed'),

    )


    # Customer who creates ticket

    customer = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE,

        related_name="tickets"

    )


    # Assigned support agent

    assigned_agent = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="assigned_tickets",

        limit_choices_to={
            "role": "agent"
        }

    )


    title = models.CharField(

        max_length=200

    )


    description = models.TextField()



    # File attachment

    attachment = models.FileField(

        upload_to="ticket_files/",

        null=True,

        blank=True

    )



    # AI predicted category

    category = models.CharField(

        max_length=20,

        choices=CATEGORY_CHOICES,

        default="general"

    )



    # AI predicted priority

    priority = models.CharField(

        max_length=20,

        choices=PRIORITY_CHOICES,

        default="medium"

    )



    # AI sentiment analysis result

    sentiment = models.CharField(

        max_length=20,

        default="Neutral"

    )



    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default="open"

    )



    created_at = models.DateTimeField(

        auto_now_add=True

    )



    def __str__(self):

        return self.title





# ==========================
# Ticket Comment / Chat Model
# ==========================

class TicketComment(models.Model):


    ticket = models.ForeignKey(

        Ticket,

        on_delete=models.CASCADE,

        related_name="comments"

    )


    user = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE

    )


    message = models.TextField()



    created_at = models.DateTimeField(

        auto_now_add=True

    )



    def __str__(self):

        return f"{self.user.username} - {self.ticket.title}"