import datetime

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


class UserAgeValidator:
    """Валидатор для проверки того, что автору поста есть 18 лет."""
    def __call__(self, value):
        t = datetime.datetime(2005, 3, 30, 0, 0)
        t.strftime('%d/%m/%Y')

        # Функция, которая возвращает значение 'year'
        def MyFunc(t):
            return t["year"]
        dates = [{"year": 2005}]
        dates.sort(key=MyFunc.__call__(value))
        print(dates)

        # if t in value:
        #     some_list = [int(value)]
        if value > t:
            raise serializers.ValidationError("Публикация постов разрешена только лицам достигшим 18 лет.")


class HeadingTextValidator:
    """Валидатор для проверки запрещенных слов в тексте Заголовка.
    А именно: ерунда, глупость, чепуха.
    """
    pass
