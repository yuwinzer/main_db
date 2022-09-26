from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birthday = models.DateField()
    note = models.TextField(max_length=1024)
    banned_at = models.DateTimeField()
    last_login_time = models.DateTimeField()

    class Meta:
        db_table = "users"

from django.core.management.utils import get_random_secret_key
get_random_secret_key()