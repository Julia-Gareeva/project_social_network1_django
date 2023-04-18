from rest_framework import serializers
import re
from datetime import date
from django.core.exceptions import ValidationError


class UserPasswordValidator:
    """Валидатор для проверки пароля пользователя."""

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'

    @staticmethod
    def validate_by_regexp(password):
        """Валидация пароля по регулярному выражению.
           Проверяет строку пароля на соответствие заданному шаблону с помощью регулярных выражений.
           Шаблон должен соответствовать желаемому формату пароля, а длина пароля должна составлять
           не менее 8 символов, по крайней мере, с одной строчной буквой, одной прописной буквой
           и одной цифрой.

           Аргументы:
           password (str): строка пароля для проверки.
           pattern (str): шаблон регулярного выражения для сопоставления с паролем.
        """
        if re.match(UserPasswordValidator.pattern, password) is None:
            raise serializers.ValidationError("Пароль имеет неправильный формат.")


class EmailValidator:
    """Валидатор для проверки почты пользователя.
       Разрешены домены: mail.ru, yandex.ru """
    def __call__(self, value):
        if value.endswith('@mail.ru') or value.endswith('@yandex.ru'):
            return value
        raise serializers.ValidationError("Разрешены адреса эл. почты только с доменными именами 'mail.ru' или 'yandex.ru'")


class AdultValidator:
    """
    Валидотор, который проверяет что автору поста есть 18 лет.
    """
    def __init__(self, message=None):
        if message is None:
            message = "Автору должно быть не менее 18 лет."
        self.message = message

    def __call__(self, value):
        birthday = value
        today = date.today()
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        if age < 18:
            raise ValidationError(self.message)


class ForbiddenWordsValidator:
    """
    Валидатор, который проверяет, содержит ли заголовок сообщения какие-либо из запрещенных слов.
    """
    def __init__(self, forbidden_words=["ерунда", "глупость", "чепуха"]):
        self.forbidden_words = forbidden_words

    def __call__(self, value):
        for word in self.forbidden_words:
            if word in value.lower():
                raise serializers.ValidationError(f"Заголовок содержит запрещенное слово '{word}'")
