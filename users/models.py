from django.db import models


# Create your models here.z
class Teacher(models.Model):
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    email = models.EmailField(max_length=55)
    bithdate = models.DateField()
    phone = models.IntegerField()
    local_address = models.TextField(max_length=200)
    permanent_address = models.TextField(max_length=200)
    username = models.CharField(max_length=24)
    password = models.CharField(max_length=30)


class Student(models.Model):
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    email = models.EmailField(max_length=55)
    bithdate = models.DateField()
    phone = models.IntegerField()
    standard = models.IntegerField()
    subject = models.CharField(max_length=30)
    local_address = models.TextField(max_length=200)
    permanent_address = models.TextField(max_length=200)
    username = models.CharField(max_length=24)
    password = models.CharField(max_length=30)
