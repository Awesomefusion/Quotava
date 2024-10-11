from django.contrib import admin
from .models import Quote, Category, Author  # Import all the necessary models


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Author)  # If using the Author model
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
