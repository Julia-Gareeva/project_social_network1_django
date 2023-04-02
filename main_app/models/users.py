from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    phone_number = models.BigIntegerField(verbose_name="Номер телефона", null=True)
    birthday = models.DateTimeField(verbose_name="Дата рождения", null=True)
    date_editing = models.DateTimeField(verbose_name="Дата редактирования", auto_now=True)
