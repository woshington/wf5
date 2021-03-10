from project.models import Project, Management
from rest_framework import mixins, viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ProjectSerializer


class ProjectViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()

