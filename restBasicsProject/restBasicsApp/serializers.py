from dataclasses import fields
from rest_framework.serializers import *
from .models import * 
from .models import User
from rest_framework import serializers
class Myserializer(ModelSerializer):
    class Meta:
        model=employee
        fields='__all__'
    def create(self, validated_data):
        return employee.objects.create(**validated_data)    


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.emp_name = validated_data.get('title', instance.emp_name)
        instance.emp_age = validated_data.get('emp_age', instance.emp_age)
        instance.emp_address = validated_data.get('emp_address', instance.emp_address)
       
        instance.save()
        return instance  




class Myserializer1(HyperlinkedModelSerializer):
    class Meta:
        model=employee
        fields='__all__'




class Myserializer2(ModelSerializer):
    class Meta:
        model=User
        fields=['id','password','username','first_name','last_name' ,'email' ]

class ExampleSerializer(Serializer):
    emp_name= models.CharField(max_length=20)
    emp_age = models.IntegerField(default=0)
    emp_number= models.IntegerField(default=000000)
    emp_address = models.CharField(max_length=200)

class UserRegisterationsSerializer(ModelSerializer):
    password2=serializers.CharField(style={'input_type': 'password'},write_only=True)
    class Meta:
        model=User
        fields='__all__'
        extra_kwargs={
            'password':{'write_only':True,}
        }
