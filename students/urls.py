from django.urls import path
from .views import StudentCourseEnrollView, StudentCourseBillingView

urlpatterns = [
    path('course/enroll/', StudentCourseEnrollView.as_view(), name='student_course_enroll'),
    path('course/billing/', StudentCourseBillingView.as_view(), name='course_billing'),
]
