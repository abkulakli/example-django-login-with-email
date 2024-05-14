from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CustomUserRegisterView, AuthenticatedView

urlpatterns = [
    path('api/register/', CustomUserRegisterView.as_view(), name="register"),
    path('api/login/', TokenObtainPairView.as_view(), name="login"),
    path('api/refresh/', TokenRefreshView.as_view(), name="refresh"),
    path('api/authenticated/', AuthenticatedView.as_view(), name="authenticated"),
]