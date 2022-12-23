from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from teachers.models import Courses
from .forms import StudentEnrollCourseModelForm
from school import settings
from django.views.generic import CreateView


# Create your views here.


class StudentCoursesEnrollCreateView(CreateView):
    # NEED IMPROVEMENTS ---->
    template_name = 'students/student_enroll_courses.html'
    model = Courses

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def get_queryset(self):
        queryset = Courses.objects.get(id=self.kwargs)
        return queryset


class StudentCourseBillingView(TemplateView):
    template_name = 'students/student_enroll_courses_billing.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_enroll'] = StudentEnrollCourseModelForm()
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return render(request, self.template_name, context)

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
