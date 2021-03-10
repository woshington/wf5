from accounts.models import User
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Mixin for create user
    Is not required authentication
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
