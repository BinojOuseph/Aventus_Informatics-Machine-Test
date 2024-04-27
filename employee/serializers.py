from .models import *
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeMaster
        fields="__all__"
