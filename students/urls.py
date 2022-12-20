from django.urls import path
from .views import StudentCourseEnrollView, StudentCourseBillingView

urlpatterns = [
    path('courses/enroll/', StudentCourseEnrollView.as_view(), name='student_course_enroll'),
    path('courses/billing/', StudentCourseBillingView.as_view(), name='course_billing'),
]
