from django.db import models

from main_app.models.users import User


class Comments(models.Model):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    author = models.ForeignKey(User, verbose_name="Автор", null=True, blank=True,
                               on_delete=models.DO_NOTHING)
    text = models.TextField(verbose_name="Текст", max_length=960)
    date_creation = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    date_editing = models.DateTimeField(verbose_name="Дата редактирования", auto_now=True)
