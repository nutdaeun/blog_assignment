from rest_framework import serializers
from accounts.models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email"]