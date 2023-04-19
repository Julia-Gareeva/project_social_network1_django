from rest_framework import serializers
from main_app.models import User
from main_app.validators import UserPasswordValidator, EmailValidator
from datetime import datetime


class UserSerializer(serializers.ModelSerializer):
    """Класс сериализации пользователя в приложении."""
    class Meta:
        model = User
        fields = "__all__"

    @staticmethod
    def validate_password(value):
        UserPasswordValidator.validate_by_regexp(value)
        return value

    class BirthdayField(serializers.Field):
        def to_internal_value(self, data):
            try:
                return datetime.strptime(data, '%d-%m-%Y').date()
            except ValueError:
                raise serializers.ValidationError('Неправильный формат даты. Используйте формат "дд-мм-гггг".')

        def to_representation(self, value):
            return value.strftime('%d-%m-%Y')

    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[EmailValidator()])
    birthday = BirthdayField()
    date_joined = serializers.SerializerMethodField()
    last_login = serializers.SerializerMethodField()
    date_editing = serializers.SerializerMethodField()

    def get_date_joined(self, obj):
        if obj.date_joined:
            return obj.date_joined.strftime("%d-%m-%Y")
        else:
            return ""

    def get_last_login(self, obj):
        if obj.last_login:
            return obj.last_login.strftime("%d-%m-%Y")
        else:
            return ""

    def get_date_editing(self, obj):
        if obj.date_editing:
            return obj.date_editing.strftime("%d-%m-%Y")
        else:
            return ""

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user
