from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):

    class Meta:

        model = Ticket

        fields = [
            "title",
            "description",
            "category",
            "priority",
            "attachment",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter ticket title"
                }
            ),


            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Describe your problem"
                }
            ),

        }