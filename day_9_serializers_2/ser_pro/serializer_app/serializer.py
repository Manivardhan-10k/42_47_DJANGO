from rest_framework import serializers 
from .models import Employee
class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"
        # fields:["emp_id","emp_name"]