from django.urls import path

from . import views

app_name = 'mytestapp'

urlpatterns = [
    path("", views.index_endpoint, name="main"),
    path("no_login_required/", views.no_login_required_endpoint, name="no_login_required_endpoint"),
    path("login_required/", views.login_required_endpoint, name="login_required_endpoint"),
]
