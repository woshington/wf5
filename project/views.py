from project.models import Project, Management
from rest_framework import mixins, viewsets, generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ProjectSerializer, ManagementSerializer, ApproveSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime


class ProjectViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()

    def get_serializer_context(self):        
        return {'request': self.request}

    @action(
        methods=['post'],
        detail=False,
        url_path='aprovar-projeto',
        permission_classes=[AllowAny],
        serializer_class=ApproveSerializer
    )
    def approve(self, request):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.data.get('code')

        try:
            project = Project.objects.get(code=code, status=1)
            project.status == 2
            project.approval_date = datetime.now()
            project.save()
            response = {
               'message': 'Projeto aprovado com sucesso!'
            }
        except Project.DoesNotExist:
            context = {
                'message': 'Projeto não encontrado!'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(response, status=status.HTTP_200_OK)

class ManagementViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = ManagementSerializer
    permission_classes = [IsAuthenticated]
    queryset = Management.objects.all()