from project.models import Project, Management
from rest_framework import serializers
from datetime import datetime


class ProjectSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()
    management = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ['user']

    def get_status(self, obj):
        return obj.get_status_display()

    def get_balance(self, obj):
        return obj.balanced
    
    def get_user(self, obj):
        return obj.user.name

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
    
    def get_management(self, obj):
        return ManagementSerializer(obj.management_set.all(), many=True).data


class ManagementSerializer(serializers.ModelSerializer):
    project = serializers.CharField(required=True, max_length=20)
    class Meta:
        model = Management
        fields = "__all__"

    def validate(self, data):
        project = data['project'].upper()

        if not Project.objects.filter(code=project).exists():
            raise serializers.ValidationError(
                "Projeto Inválido"
            )

        return data

    def create(self, validated_data):
        """
        Override method for create management
        When saving the management, it checks the status of the linked project
        if status == 1, change the status to 2 and save the current date
        in the approval_date property
        """
        validated_data['project'] = Project.objects.get(
            code=validated_data['project'].upper()
        )
        management = Management.objects.create(**validated_data)
        project = management.project
        if project.status == 1:
            project.status = 2
            project.approval_date = datetime.now()
            project.save()

        return management
    
    def update(self, instance, validated_data):
        validated_data['project'] = Project.objects.get(
            code=validated_data['project'].upper()
        )
        instance = super(ManagementSerializer,self).update(instance, validated_data)
        return instance

class ApprovalSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, max_length=20)
    budget = serializers.DecimalField(
        max_digits=9, decimal_places=2, required=True,
        min_value=0
    )
    spent = serializers.DecimalField(
        max_digits=9, decimal_places=2, required=True,
        min_value=0
    )
    
    class Meta:
        model = Project
        fields = ['code', 'budget', 'spent']

    def validate(self, data):
        project = data['code'].upper()

        if not Project.objects.filter(
                code=project, status=1).exists():
            raise serializers.ValidationError(
                "Projeto Inválido!"
            )

        return data

    
class CodeProjectSerializer(serializers.Serializer):
    code = serializers.CharField(required=True, max_length=20)
