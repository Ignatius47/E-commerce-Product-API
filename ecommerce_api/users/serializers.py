from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser  # Use your CustomUser model
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for user profile details.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
