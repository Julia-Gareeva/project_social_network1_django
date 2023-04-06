from rest_framework import serializers

from main_app.models import User
from main_app.validators import UserPasswordValidator, UserEmailValidator


class UserSerializer(serializers.ModelSerializer):
    """Класс сериализации пользователя в приложении."""
    class Meta:
        model = User
        fields = "__all__"

    password = serializers.CharField(validators=[UserPasswordValidator()])
    email = serializers.EmailField(validators=[UserEmailValidator()])
