"""
Модели для приложения "Jobs" (выполненные работы).
"""

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from base.models import TimeStampMixin


class Job(TimeStampMixin):
    """
    Модель для хранения данных о работах.
    """

    image = models.ImageField(
        upload_to="images/",
        verbose_name="Изображение",
        help_text="Изображение для демонстрации работы",
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание",
        help_text="Краткое описание выполненной работы",
    )
    elaborate_description = RichTextUploadingField(
        verbose_name="Подробное описание",
        help_text="Подробное описание выполненной работы",
        default="Подробное описание работы",
    )

    class Meta:
        verbose_name = "Выполненная работа"
        verbose_name_plural = "Выполненные работы"

    def __str__(self) -> str:
        return f'Объект "Выполненная работа" (id={self.pk})'

    def summary(self) -> str:
        """
        Краткое содержание выполненной работы.
        :return:
        """

        return self.elaborate_description[:100] + "..."
