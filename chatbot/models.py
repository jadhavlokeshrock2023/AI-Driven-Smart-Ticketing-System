from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings


class ChatConversation(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    message = models.TextField()

    response = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.user.username
    
from django.db import models


class KnowledgeBase(models.Model):

    question = models.CharField(
        max_length=255
    )

    answer = models.TextField()


    category = models.CharField(
        max_length=50,
        default="general"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.question    