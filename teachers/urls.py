from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.teacher_courses, name='teacher_course'),
    path('course/added/', views.course_success_add, name='course_success'),
]
