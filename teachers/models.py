from django.db import models


class Courses(models.Model):
    course_name = models.CharField(max_length=255)
    standard = models.IntegerField()
    course_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course_type = models.CharField(max_length=10)
    price = models.IntegerField()
    teacher_name = models.CharField(max_length=120)
