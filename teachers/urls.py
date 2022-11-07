from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.teacher_register, name='teacher_reg'),
    path('login/', views.teacher_login, name='teacher_log'),
    path('', views.teacher_register)
]
