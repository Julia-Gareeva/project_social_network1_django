from rest_framework import routers
from django.urls import path

from main_app import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
router.register(r"user", views.UserView),
router.register(r"publication", views.PublicationsView),
router.register(r"comment", views.CommentsView),

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + router.urls
