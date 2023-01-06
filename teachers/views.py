from django.shortcuts import render, redirect
from .forms import TeacherCoursesModelForm
from django.http import HttpResponse
from users.models import USER_CHOICE_VALUE_STUDENT, USER_CHOICE_VALUE_TEACHER
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Courses
from django.http import JsonResponse
from django.views.generic import DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


def teacher_courses(request):
    if request.user.user_type == USER_CHOICE_VALUE_TEACHER:
        if request.method == "POST":
            course_form = TeacherCoursesModelForm(request.POST)
            if course_form.is_valid():
                final_course_save = course_form.save(commit=False)
                final_course_save.teacher = request.user
                final_course_save.save()
                return redirect('course_success')
        else:
            course_form = TeacherCoursesModelForm()
    else:
        return HttpResponse("You Are Not Teacher....")
    return render(request, 'teachers/teacher_courses_add.html', {'form': course_form})


def course_success_add(request):
    return render(request, 'teachers/course_added_success.html')


class CoursesManageView(LoginRequiredMixin, ListView):
    login_url = '/users/login'
    model = Courses
    template_name = 'teachers/manage_courses.html'
    context_object_name = 'course_data'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset(request)
        context = super().get_context_data(**kwargs)
        # instance = context.get('course_data')[0]
        context['form'] = TeacherCoursesModelForm()
        return render(request, self.template_name, context)

    # Override get_queryset for filtering current login teacher courses
    def get_queryset(self, request):
        qs = super().get_queryset()
        current_login_teacher_courses = qs.filter(teacher=request.user)
        return current_login_teacher_courses


class CoursesDeleteView(DeleteView):
    model = Courses

    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Get Request Forbidden </h1>")

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        object.delete()
        data = {'success': 'OK'}
        return JsonResponse(data)


class CoursesUpdateView(UpdateView):
    model = Courses
    form_class = TeacherCoursesModelForm
    success_url = "/teachers/courses/manage"

    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1> GET Request Forbidden, Only POST request support </h1>")

    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'data': form.cleaned_data
        })
