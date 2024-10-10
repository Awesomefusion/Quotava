from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)


class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Quote(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
