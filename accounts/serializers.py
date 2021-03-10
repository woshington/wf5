from accounts.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for data user
    """
    class Meta:
        model = User
        exclude = ["last_login"]

    def validate(self, data):
        """
        Verification of password size
        Return: exception if size is violated
        Return: data user if size is valid
        """
        password = data['password']
        if len(password) > 12:
            raise serializers.ValidationError(
                "A senha deve possuir no máximo 12 caracteres!"
            )
        return data

    def create(self, validated_data):
        """
        Override method for create user
        Invokes the created method in User Model
        this is necessary to make hashear password
        """
        user = User.objects.create_user(**validated_data)
        return user
