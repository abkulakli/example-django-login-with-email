# customauth/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
