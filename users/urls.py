from django.urls import path
from . import views


urlpatterns = [
    path('login/student/', views.student_login, name='student_login'),
    path('login/teacher/', views.teacher_login, name='teacher_login'),
    path('registration/student/', views.student_registration, name='student_reg'),
    path('registration/teacher/', views.teacher_registration, name='teacher_reg'),
    path('logged/', views.user_logged, name='school_user_logged'),

]
