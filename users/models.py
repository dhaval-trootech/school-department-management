from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.z
class SchoolUser(AbstractUser):
    USER_CHOICE = [('T', 'Teacher User'),
                   ('S', 'Student User'),
                   ]
    bithdate = models.DateField()
    phone = models.IntegerField()
    standard = models.IntegerField()
    subject = models.CharField(max_length=30)
    local_address = models.TextField(max_length=200)
    permanent_address = models.TextField(max_length=200)
    users_code = models.CharField(max_length=5, choices=USER_CHOICE)
