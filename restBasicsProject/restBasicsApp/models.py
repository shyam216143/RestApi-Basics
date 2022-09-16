from pyexpat import model
from django.db import models

# Create your models here.
class employee(models.Model):
    emp_name= models.CharField(max_length=20)
    emp_age = models.IntegerField(default=0)
    emp_number= models.IntegerField(default=000000)
    emp_address = models.CharField(max_length=200)
    

    def __str__(self) -> str:
        return self.emp_name




class student(models.Model):
    name= models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    roll= models.IntegerField(default=000000)
    address = models.CharField(max_length=200)
    

    def __str__(self) -> str:
        return self.name