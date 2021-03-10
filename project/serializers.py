from project.models import Project, Management
from rest_framework import serializers
from datetime import datetime


class ProjectSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()

    class Meta:
        model = Project
        exclude = ['user']

    def get_status(self, obj):
        return obj.get_status_display()

    def get_balance(self, obj):
        return obj.balanced

    def validate(self, data):
        """
        Verification of the code characters
        Return: exception if characters is not alphanumeric or
        data of project if characters is valid
        """
        code = data['code']
        if not code.isalnum():
            raise serializers.ValidationError(
                "Permitido apenas letras e números!"
            )
        return data

    def create(self, validated_data):
        """
        Override method for create project
        get authenticated user sent by the viewset
        add the user to project.user before save.
        Futhermore, transforms the code in upper
        """
        user = self.context['request'].user
        project = Project(**validated_data)
        project.user = user
        project.code = project.code.upper()
        project.save()
        return project


class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = "__all__"

    def create(self, validated_data):
        """
        Override method for create management
        When saving the management, it checks the status of the linked project
        if status == 1, change the status to 2 and save the current date
        in the approval_date property
        """
        management = Management.objects.create(**validated_data)
        project = management.project
        if project.status == 1:
            project.status = 2
            project.approval_date = datetime.now()
            project.save()
        return management


class CodeProjectSerializer(serializers.Serializer):
    code = serializers.CharField(required=True, max_length=20)
