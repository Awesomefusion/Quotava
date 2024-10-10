from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Quote, Author, Category, User
from .serializers import QuoteSerializer, AuthorSerializer, CategorySerializer, UserSerializer


class BaseViewSet(viewsets.ModelViewSet):
    """
    A base viewset that implements DRY permissions logic
    """
    permission_classes_by_action = {}

    def get_permissions(self):
        try:
            # Return the permission classes based on the action
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # If action is not explicitly defined, use the default permission class
            return [permission() for permission in self.permission_classes]


class QuoteViewSet(BaseViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    permission_classes_by_action = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsAuthenticated],
        'update': [IsAuthenticated],
        'partial_update': [IsAuthenticated],
        'destroy': [IsAdminUser],  # Only admins can delete quotes
    }


class AuthorViewSet(BaseViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    permission_classes_by_action = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsAuthenticated],
        'update': [IsAuthenticated],
        'partial_update': [IsAuthenticated],
        'destroy': [IsAdminUser],  # Only admins can delete authors
    }


class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes_by_action = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsAuthenticated],
        'update': [IsAuthenticated],
        'partial_update': [IsAuthenticated],
        'destroy': [IsAdminUser],  # Only admins can delete categories
    }


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes_by_action = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsAdminUser],  # Only admins can create users
        'update': [IsAuthenticated],
        'partial_update': [IsAuthenticated],
        'destroy': [IsAdminUser],  # Only admins can delete users
    }
