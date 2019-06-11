from rest_framework import serializers
from .models import Emp

# This Userdefined Serializer Class
class EmpSerializer(serializers.ModelSerializer):
    class Meta :
        model = Emp
        fields = '__all__'

