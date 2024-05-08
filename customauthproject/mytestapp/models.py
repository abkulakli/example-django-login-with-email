from django.db import models


class MyTestAppPermissions(models.Model):
    name = models.CharField(max_length=100)
    codename = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        permissions = [
            ("can_view_permission_required_page", "Can view permission required page"),
        ]
