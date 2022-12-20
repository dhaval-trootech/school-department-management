from django.urls import path
from . import views

urlpatterns = [
    path('courses/add', views.teacher_courses, name='teacher_course'),
    path('courses/added/', views.course_success_add, name='course_success'),
    path('courses/manage/', views.CoursesManageView.as_view(), name='course_manage'),
    path('course/manage/delete/<int:course_del_id>/', views.CoursesDeleteView.as_view(), name='course_delete'),
]
