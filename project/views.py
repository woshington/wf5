from project.models import Project, Management
from rest_framework import mixins, viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ProjectSerializer, ManagementSerializer


class ProjectViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()

    def get_serializer_context(self):        
        return {'request': self.request}


class ManagementViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = ManagementSerializer
    permission_classes = [IsAuthenticated]
    queryset = Management.objects.all()