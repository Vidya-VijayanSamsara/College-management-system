from django.db import models

# Create your models here.
class Admin(models.Model):
    admin_name=models.CharField(max_length=20)
    admin_username=models.CharField(max_length=20)
    admin_mail=models.CharField(max_length=20)
    admin_qualification=models.CharField(max_length=20)
    admin_post=models.CharField(max_length=20)
    admin_yoj=models.CharField(max_length=20)
    admin_experience=models.CharField(max_length=20)
    admin_place=models.CharField(max_length=20)
class Student(models.Model):
    student_name = models.CharField(max_length=20)
    student_username = models.CharField(max_length=20)
    student_mail = models.CharField(max_length=20)
class Staff(models.Model):
    staff_name = models.CharField(max_length=20)
    staff_username = models.CharField(max_length=20)
    staff_mail = models.CharField(max_length=20)
class Login(models.Model):
    username=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
    status=models.IntegerField()