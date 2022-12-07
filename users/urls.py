from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.users_login, name='users_login'),
    path('logout/', views.log_out, name='logout'),
    path('registration/', views.choose_user, name='choose_user'),
    path('registration/student/', views.student_registration, name='student_reg'),
    path('registration/teacher/', views.teacher_registration, name='teacher_reg'),
    path('submitted/', views.thanks_submission, name='user_submit'),
    path('password_reset/', views.user_change_pass, name='user_change_pass'),

]
