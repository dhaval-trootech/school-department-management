from django.urls import path
from . import views


urlpatterns = [
    path('registration/', views.school_user_registration, name='school_user_reg')
]
