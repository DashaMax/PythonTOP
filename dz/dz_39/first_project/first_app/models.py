from django.contrib.auth.models import User
from django.db import models


class PasswordModel(models.Model):
    password = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} password'
