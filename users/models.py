from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.z
class SchoolUser(AbstractUser):
    USER_CHOICE = [('T', 'Teacher'),
                   ('S', 'Student'),
                   ]
    birthdate = models.DateField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    standard = models.IntegerField(null=True, blank=True)
    subject = models.CharField(max_length=30, blank=True)
    local_address = models.TextField(max_length=200, blank=True)
    permanent_address = models.TextField(max_length=200, blank=True)
    user_type = models.CharField(max_length=10, choices=USER_CHOICE, default='Unknown')

    REQUIRED_FIELDS = ['phone', 'local_address']
