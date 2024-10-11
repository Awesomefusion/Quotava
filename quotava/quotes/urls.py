from django.urls import path
from .views import QuoteListCreateView, QuoteDetailView, CategoryListCreateView, CategoryDetailView, UserListCreateView, UserDetailView

urlpatterns = [
    # Quotes endpoints
    path('quotes/', QuoteListCreateView.as_view(), name='quote-list-create'),  # Note the trailing slash
    path('quotes/<int:pk>/', QuoteDetailView.as_view(), name='quote-detail'),

    # Categories endpoints
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Users endpoints
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
