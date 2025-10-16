from django.db import models

# Create your models here.


class Student(models.Model): ##atrributes-> field    
    stu_id= models.IntegerField(primary_key=True)
    stu_name=models.CharField(max_length=50)
    stu_branch=models.CharField(max_length=20)
    stu_mob=models.CharField(max_length=10,unique=True)
    
