from rest_framework import serializers
from authapp.models import CustomUser


class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'role']
