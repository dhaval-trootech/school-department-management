from django.db import models


class Courses(models.Model):
    order_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255, blank=True)
    teacher_name = models.CharField(max_length=120, blank=True)
    student_name = models.CharField(max_length=255)
    student_email = models.EmailField(max_length=55)
    student_address = models.CharField(max_length=60)
    student_city = models.CharField(max_length=30)
    student_state = models.CharField(max_length=30)
    student_zip = models.IntegerField()
    student_standard = models.IntegerField(blank=True)
    enroll_time = models.DateTimeField(auto_now_add=True)
    course_type = models.CharField(max_length=10, blank=True)
    course_price = models.IntegerField(blank=True)
