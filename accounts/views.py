from accounts.models import User
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer, UserUpdateSerializer


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Mixin for create user
    Is not required authentication
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def get_object(self):
        return self.request.user

    @action(
        methods=['put'],
        detail=False,
        url_path='current',
        permission_classes=[IsAuthenticated],
        serializer_class = UserUpdateSerializer
    )
    def put_current(self, request, *args, **kwargs):
        context = {'request': self.request}
        user = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(user, data=data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)