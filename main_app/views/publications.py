from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from main_app.models import Publications
from main_app.permissions import PermissionPolicyMixin, IsOwner
from main_app.serializers import PublicationsSerializer


class PublicationsView(PermissionPolicyMixin, ModelViewSet):
    """CRUD для публикации/поста в приложении."""
    queryset = Publications.objects.all()
    serializer_class = PublicationsSerializer
    permission_classes_per_method = {
        "list": [AllowAny],
        "create": [IsAuthenticated],
        "update": [IsOwner or IsAdminUser],
        "destroy": [IsOwner or IsAdminUser],
        "retrieve": [AllowAny],
    }
