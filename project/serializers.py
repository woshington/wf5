from project.models import Project, Management
from rest_framework import serializers
from datetime import datetime

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["code", "name", "description"]
    
    def validate(self, data):
        code = data['code']
        if not code.isalnum():
            raise serializers.ValidationError("Código aceita apenas letras e números!")
        return data

    def create(self, validated_data):
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
        management = Management.objects.create(**validated_data)
        project = management.project
        if project.status == 1:
            project.status = 2
            project.approval_date = datetime.now()
            project.save()
        return management

class ApproveSerializer(serializers.Serializer):
    code = serializers.CharField(required=True, max_length=20)
