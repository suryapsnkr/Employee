from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from shree.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
