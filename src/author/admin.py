"""
Функции панели управления для приложения "Автор".
"""

from django.contrib import admin

from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "resume_url",
        "github_url",
        "email",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )