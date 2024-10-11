from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Quote Model
class Quote(models.Model):
    author = models.TextField()
    content = models.TextField()
    category = models.TextField()

    def __str__(self):
        return f'"{self.content}" - {self.author.name}'


class User(AbstractUser):
    # Override groups and user_permissions with unique related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Change the related_name to avoid clashes
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Change the related_name to avoid clashes
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
