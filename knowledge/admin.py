from django.contrib import admin

from .models import KnowledgeArticle



@admin.register(KnowledgeArticle)
class KnowledgeArticleAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "created_at"
    )