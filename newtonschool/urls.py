from django.urls import path
from . import views


urlpatterns = [
    path('schoolform/', views.school_model_form, name='school_form')
]
