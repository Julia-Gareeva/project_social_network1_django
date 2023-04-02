from django.db import models

from main_app.models.comments import Comments
from main_app.models.users import User


class Publications(models.Model):
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    heading = models.CharField(verbose_name="Заголовок", max_length=210)
    text = models.TextField(verbose_name="Текст", max_length=2200)
    image = models.ImageField(verbose_name="Изображение", upload_to="images/", max_length=110, blank=True)
    author = models.ForeignKey(User, verbose_name="Автор", null=True, blank=True,
                               on_delete=models.DO_NOTHING)
    comments = models.ForeignKey(Comments, verbose_name="Комментарий", null=True,
                                 blank=True, on_delete=models.DO_NOTHING)
    date_creation = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    date_editing = models.DateTimeField(verbose_name="Дата редактирования", auto_now=True)