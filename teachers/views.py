from django.shortcuts import render, redirect
from .forms import TeacherCoursesModelForm
from django.http import HttpResponse
from users.models import USER_CHOICE_VALUE_STUDENT, USER_CHOICE_VALUE_TEACHER
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Courses


# Create your views here.

def teacher_courses(request):
    if request.user.user_type == USER_CHOICE_VALUE_TEACHER:
        if request.method == "POST":
            course_form = TeacherCoursesModelForm(request.POST)
            if course_form.is_valid():
                course_db = course_form.save(commit=False)
                course_db.teacher_name = request.user.get_full_name()
                course_db.save()
                return redirect('course_success')
        else:
            course_form = TeacherCoursesModelForm()
    else:
        return HttpResponse("You Are Not Teacher....")
    return render(request, 'teachers/teacher_courses.html', {'courses_fm': course_form})


def course_success_add(request):
    return render(request, 'teachers/course_added_success.html')


class CoursesManageView(TemplateView):
    template_name = 'teachers/manage_courses.html'

    def get(self, request, *args, **kwargs):
        course_data = Courses.objects.all()
        return render(request, self.template_name, {'course_data': course_data})


class CoursesDeleteView(TemplateView):

    def get(self, request, course_del_id):
        Courses.objects.get(id=course_del_id).delete()
        return HttpResponseRedirect(reverse('course_manage'))
