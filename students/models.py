from django.db import models


class CoursePurchases(models.Model):
    user = models.ForeignKey('teachers.courses', on_delete=models.CASCADE)

    # teacher_name = models.CharField(max_length=120, blank=True)
    # student_name = models.CharField(max_length=255)
    # student_email = models.EmailField(max_length=55)
    # student_address = models.CharField(max_length=60)
    student_zip = models.IntegerField()
    # student_standard = models.IntegerField(blank=True)
    enroll_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student_courses_purchase'
