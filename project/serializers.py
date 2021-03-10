from project.models import Project, Management
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["code", "name", "description"]
    
    def create(self, validated_data):
        user = self.context['request'].user
        project = Project(**validated_data)
        project.user = user
        project.save()
        return project