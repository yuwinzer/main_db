from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    note = models.TextField(max_length=1024, blank=True)
    banned_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "users"
