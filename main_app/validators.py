from rest_framework import serializers


class UserPasswordValidator:
    """Валидатор для проверки пароля пользователя."""
    def __call__(self, value):
        if len(str(value)) != 8:
            raise serializers.ValidationError("Пароль должен быть не менее 8 символов, должен включать цифры.")

        if int(len(value)) != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            raise serializers.ValidationError("Пароль должен быть не менее 8 символов, должен включать цифры.")


class UserEmailValidator:
    """Валидатор для проверки почты пользователя."""
    pass


class PublicationsUserValidator:
    """Валидатор для проверки того, что автору поста есть 18 лет."""
    pass


class HeadingTextValidator:
    """Валидатор для проверки запрещенных слов в тексте Заголовка.
    А именно: ерунда, глупость, чепуха.
    """
    pass
