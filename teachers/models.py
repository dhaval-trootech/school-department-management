from django.db import models


class Courses(models.Model):
    COURSE_TYPE_CHOICES = [('free', 'FREE'),
                           ('paid', 'PAID')]
    course_name = models.CharField(max_length=255)
    standard = models.IntegerField()
    course_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course_type = models.CharField(max_length=10, choices=COURSE_TYPE_CHOICES)
    price = models.IntegerField()
    user = models.ForeignKey('users.SchoolUser', on_delete=models.CASCADE, limit_choices_to={'user_type': 'T'})

    def __str__(self):
        return self.course_name
