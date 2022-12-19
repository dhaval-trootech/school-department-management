from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from teachers.models import Courses
from .forms import StudentEnrollCourseModelForm


# Create your views here.
class StudentCourseEnrollView(TemplateView):
    template_name = 'students/student_enroll_courses.html'

    def get_context_data(self, **kwargs):
        context = super(StudentCourseEnrollView, self).get_context_data(**kwargs)
        context['courses'] = Courses.objects.all()
        return context


class StudentCourseBillingView(TemplateView):
    template_name = 'students/student_enroll_courses_billing.html'

    def get_context_data(self, **kwargs):
        context = super(StudentCourseBillingView, self).get_context_data(**kwargs)
        context['student_enroll'] = StudentEnrollCourseModelForm()
        return context

    def get(self, request, *args, **kwargs):
        student_enroll = StudentEnrollCourseModelForm()
        return render(request, self.template_name, {'student_enroll': student_enroll})

    def post(self, request, *args, **kwargs):
        student_enroll = StudentEnrollCourseModelForm(request.POST)
        if student_enroll.is_valid():
            stu_enroll_model_object = student_enroll.save(commit=False)
            stu_enroll_model_object.student_standard = request.user.standard
            stu_enroll_model_object.price = 0
            # Final Database Save
            stu_enroll_model_object.save()

            return HttpResponseRedirect(reverse('school_dashboard'))
        else:
            return render(request, self.template_name, {'student_enroll': student_enroll})
