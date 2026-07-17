from django.contrib import admin

from .models import (
    ChatConversation,
    KnowledgeBase
)


admin.site.register(
    ChatConversation
)


admin.site.register(
    KnowledgeBase
)