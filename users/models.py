from django.db import models
from django.contrib.auth.models import AbstractUser

USER_CHOICE_VALUE_STUDENT = 'S'
USER_CHOICE_VALUE_TEACHER = 'T'


# Create your models here.
class SchoolUser(AbstractUser):
    USER_CHOICE = [(USER_CHOICE_VALUE_TEACHER, 'Teacher'),
                   (USER_CHOICE_VALUE_STUDENT, 'Student'),
                   ]
    birthdate = models.DateField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    standard = models.IntegerField(null=True, blank=True)
    subject = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    local_address = models.TextField(max_length=200, blank=True)
    permanent_address = models.TextField(max_length=200, blank=True)
    user_type = models.CharField(max_length=10, choices=USER_CHOICE)
    terms_conditions = models.BooleanField(default=False)
    user_icon = models.ImageField(upload_to='images/profile-icon', blank=True)

    REQUIRED_FIELDS = ['local_address', 'email']
