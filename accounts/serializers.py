from accounts.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["last_login"]

    def validate(self, data):
        password = data['password']
        if len(password)>12:
            raise serializers.ValidationError("A senha deve possuir no máximo 12 caracteres!")
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user