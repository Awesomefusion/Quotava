from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User model to match the schema in the document
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.author_name


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Quote(models.Model):
    quote_text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.quote_text


class QuoteCategories(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('quote', 'category'),)
