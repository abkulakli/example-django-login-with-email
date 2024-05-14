from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    CustomUserRegisterView,
    AuthenticatedView,
    Permission1GrantedView,
    Permission2GrantedView,
    Permission3GrantedView,
)

urlpatterns = [
    path("api/register/", CustomUserRegisterView.as_view(), name="register"),
    path("api/login/", TokenObtainPairView.as_view(), name="login"),
    path("api/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api/authenticated/", AuthenticatedView.as_view(), name="authenticated"),
    path("api/permission/granted/1", Permission1GrantedView.as_view(), name="permission1granted"),
    path("api/permission/granted/2", Permission2GrantedView.as_view(), name="permission2granted"),
    path("api/permission/granted/3", Permission3GrantedView.as_view(), name="permission3granted"),
]
