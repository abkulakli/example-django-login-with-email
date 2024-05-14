from django.urls import path
from .views import CustomUserCreate

urlpatterns = [
    path('api/create/', CustomUserCreate.as_view(), name="create"),
]