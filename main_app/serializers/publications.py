from rest_framework import serializers

from main_app.models import Publications, User, Comments
from main_app.validators import UserAgeValidator


class PublicationsSerializer(serializers.ModelSerializer):
    """Класс сериализации публикации/поста в приложении."""
    class Meta:
        model = Publications
        fields = "__all__"

    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="first_name" + "last_name",
        validators=[UserAgeValidator()]
    )

    comments = serializers.SlugRelatedField(
        queryset=Comments.objects.all(),
        slug_field="author" + "text"
    )
