from rest_framework import serializers

from main_app.models import User


class UserSerializer(serializers.ModelSerializer):
    """Класс сериализации пользователя в приложении."""
    class Meta:
        model = User
        fields = "__all__"
