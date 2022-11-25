from django.urls import path
from . import views


urlpatterns = [
    path('', views.newton_school_dashboard, name='school_dashboard'),
    path('about/', views.newton_school_about, name='school_about'),

]
