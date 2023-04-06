from rest_framework import serializers

from main_app.models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    """Класс сериализации комментария в приложении."""
    class Meta:
        model = Comments
        fields = "__all__"

