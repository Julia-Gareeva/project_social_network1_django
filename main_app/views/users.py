from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from main_app.models import User
from main_app.permissions import PermissionPolicyMixin, IsOwner
from main_app.serializers import UserSerializer


class UserView(PermissionPolicyMixin, ModelViewSet):
    """CRUD для пользователей в приложении."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes_per_method = {
        "list": [IsAuthenticated or IsAdminUser],
        "create": [AllowAny],
        "update": [IsOwner or IsAdminUser],
        "destroy": [IsAdminUser],
        "retrieve": [IsAuthenticated or IsAdminUser],
    }
