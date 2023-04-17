from rest_framework import serializers

from main_app.models import Publications, User, Comments
from main_app.validators import ForbiddenWordsValidator, AdultValidator


class PublicationsSerializer(serializers.ModelSerializer):
    """Класс сериализации публикации/поста в приложении."""
    class Meta:
        model = Publications
        fields = ["id", "heading", "text", "author", "comments", "image", "date_creation", "date_editing"]

    heading = serializers.CharField(validators=[ForbiddenWordsValidator()])

    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="full_name",
        validators=[AdultValidator()]
    )

    comments = serializers.SlugRelatedField(
        queryset=Comments.objects.all(),
        slug_field="author"
    )
