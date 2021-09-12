from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Manages user data: User can be admin or general user
    """
    username = models.CharField(max_length=255, unique=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return "{}".format(self.username) + "-" + str(self.pk)

