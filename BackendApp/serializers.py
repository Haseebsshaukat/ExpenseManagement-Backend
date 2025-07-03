from rest_framework import serializers
from BackendApp.models import Department,Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ['id', 'is_active']
        extra_kwargs = {
            'name': {'error_messages': {'blank': 'Department name cannot be blank.'}},
            'is_active': {'error_messages': {'invalid': 'Invalid value for is_active.'}}
        }

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ['id', 'is_active']
        extra_kwargs = {
            'name': {'error_messages': {'blank': 'Employee name cannot be blank.'}},
            'salary': {'error_messages': {'invalid': 'Invalid salary value.'}},
            'employment_type': {'error_messages': {'invalid_choice': 'Invalid employment type.'}}
        }
        