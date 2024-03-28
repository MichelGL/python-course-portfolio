"""
Модели для приложения "Author".
"""

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from base.models import TimeStampMixin


class Author(TimeStampMixin):
    """
    Модель для хранения данных об авторе.
    """

    resume_url = models.URLField(help_text="Ссылка на резюме", verbose_name="Резюме",)
    github_url = models.URLField(help_text="Ссылка на GitHub", verbose_name="GitHub",)
    email = models.EmailField(verbose_name="Электронная почта",)

    class Meta:
        verbose_name = "Информация об авторе"

    def __str__(self) -> str:
        return f'Объект "Автор" (id={self.pk})'