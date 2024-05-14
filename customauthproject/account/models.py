from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class CustomPermission(models.Model):
    class Meta:
        permissions = (("permission1", "Can perform tasks requiring permission1"),
                       ("permission2", "Can perform tasks requiring permission2"),
                       ("permission3", "Can perform tasks requiring permission3"))
