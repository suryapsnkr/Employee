from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from shree.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
        
