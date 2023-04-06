from rest_framework import serializers
import re


class UserPasswordValidator:
    """Валидатор для проверки пароля пользователя."""
    # Проверяет наличие символов в обоих регистрах,
    # числел и минимальную длину 8 символов
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'

    @staticmethod
    def validate_by_regexp(password, pattern):
        """Валидация пароля по регулярному выражению."""
        if re.match(pattern, password) is None:
            raise serializers.ValidationError("Пароль имеет неправильный формат.")


class UserEmailValidator:
    """Валидатор для проверки почты пользователя.
       Разрешены домены: mail.ru, yandex.ru"""
    def __call__(self, value):
        if "mail.ru" not in str(value):
            raise serializers.ValidationError("Разрешены адреса эл. почты только с доменными именами 'mail.ru' или 'yandex.ru'")

        if "yandex.ru" not in str(value):
            raise serializers.ValidationError("Разрешены адреса эл. почты только с доменными именами 'mail.ru' или 'yandex.ru'")


class PublicationsUserValidator:
    """Валидатор для проверки того, что автору поста есть 18 лет."""
    pass


class HeadingTextValidator:
    """Валидатор для проверки запрещенных слов в тексте Заголовка.
    А именно: ерунда, глупость, чепуха.
    """
    pass
