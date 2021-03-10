from datetime import datetime
from django.db.models import Sum, F
from rest_framework import mixins, viewsets, generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from project.models import Project, Management
from .serializers import (
    ProjectSerializer, ManagementSerializer, CodeProjectSerializer,
    ApprovalSerializer
)


class ProjectViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()

    def get_serializer_context(self):
        """
        Sending data of request to ProjectSerializer
        """
        return {'request': self.request}

    @action(
        methods=['post'],
        detail=False,
        url_path='approval',
        permission_classes=[IsAuthenticated],
        serializer_class=ApprovalSerializer
    )
    def approve(self, request):
        """
        Method to approve project
        in the request is necessary to send the project code, the budget
        and the spent.
        if the code is from a new project, change the status to approved
        and approval_date to current data
        """
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.data.get('code')
        data_management = {
            'budget': serializer.data.get('budget'),
            'spent': serializer.data.get('spent')
        } 

        try:
            project = Project.objects.get(code=code.upper(), status=1)
            project.status = 2
            project.approval_date = datetime.now()
            project.save()
            data_management['project'] = project
            Management.objects.create(**data_management)
            response = {
               'message': 'Projeto aprovado com sucesso!'
            }
        except Project.DoesNotExist:
            context = {
                'message': 'Projeto não encontrado!'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        return Response(response, status=status.HTTP_200_OK)

    @action(
        methods=['post'],
        detail=False,
        url_path='cancel',
        permission_classes=[IsAuthenticated],
        serializer_class=CodeProjectSerializer
    )
    def cancel(self, request):
        """
        Method to cancel project
        in the request is necessary to send the project code
        if the code is from a new project, change the status to canceled
        and cancellation_date to current data
        """
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.data.get('code')

        try:
            project = Project.objects.get(code=code.upper(), status__in=[1, 2])
            project.status = 3
            project.cancellation_date = datetime.now()
            project.save()
            response = {
               'message': 'Projeto cancelado com sucesso!'
            }
        except Project.DoesNotExist:
            context = {
                'message': 'Projeto não encontrado!'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        return Response(response, status=status.HTTP_200_OK)

    @action(
        methods=['get'],
        detail=False,
        url_path='positive_balance',
        permission_classes=[IsAuthenticated],
        serializer_class=ProjectSerializer
    )
    def positive_balance(self, request, *args, **kwargs):
        """
        Return: data of projects that positive balance
        """
        projects = Project.objects.annotate(
            balance=Sum(F('management__budget')-F('management__spent'))
        ).filter(balance__gt=0, status=2)
        data = self.get_serializer(projects, many=True).data
        return Response(data)


class ManagementViewSet(viewsets.ModelViewSet):
    serializer_class = ManagementSerializer
    permission_classes = [IsAuthenticated]
    queryset = Management.objects.all()
