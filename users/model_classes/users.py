from django.db import models


class Users(models.Model):

    name = models.CharField(max_length=64)
    username = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=32)

    class Meta:
        db_table = 'users'
        managed = True
