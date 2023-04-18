from rest_framework import serializers

from main_app.models import User
from main_app.validators import UserPasswordValidator, EmailValidator


class UserSerializer(serializers.ModelSerializer):
    """Класс сериализации пользователя в приложении."""
    class Meta:
        model = User
        fields = "__all__"

    @staticmethod
    def validate_password(value):
        UserPasswordValidator.validate_by_regexp(value)
        return value

    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[EmailValidator()])
