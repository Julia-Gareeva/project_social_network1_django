from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from main_app.models import Comments
from main_app.permissions import PermissionPolicyMixin, IsOwner
from main_app.serializers import CommentsSerializer


class CommentsView(PermissionPolicyMixin, ModelViewSet):
    """CRUD для комментариев в приложении."""
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes_per_method = {
        "list": [AllowAny],
        "create": [IsAuthenticated],
        "update": [IsOwner or IsAdminUser],
        "destroy": [IsOwner or IsAdminUser],
        "retrieve": [AllowAny],
    }
