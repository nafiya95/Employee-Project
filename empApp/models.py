from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmployeeModel(models.Model):
    emp_name=models.CharField(max_length=200)
    emp_email=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    joining_date=models.DateField(auto_now_add=True)

    
    
