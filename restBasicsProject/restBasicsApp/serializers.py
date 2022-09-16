from dataclasses import fields
from rest_framework.serializers import *
from .models import * 


class Myserializer(ModelSerializer):
    class Meta:
        model=employee
        fields='__all__'
    def create(self, validated_data):
        return employee.objects.create(**validated_data)    
        




class Myserializer1(HyperlinkedModelSerializer):
    class Meta:
        model=employee
        fields='__all__'





class ExampleSerializer(Serializer):
    emp_name= models.CharField(max_length=20)
    emp_age = models.IntegerField(default=0)
    emp_number= models.IntegerField(default=000000)
    emp_address = models.CharField(max_length=200)