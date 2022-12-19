from django.shortcuts import render, redirect
from .forms import TeacherCoursesModelForm
from django.http import HttpResponse
from users.models import USER_CHOICE_VALUE_STUDENT, USER_CHOICE_VALUE_TEACHER


# Create your views here.

def teacher_courses(request):
    if request.user.user_type == USER_CHOICE_VALUE_TEACHER:
        if request.method == "POST":
            course_form = TeacherCoursesModelForm(request.POST)
            if course_form.is_valid():
                course_db = course_form.save(commit=False)
                course_db.teacher_name = request.user.username
                course_db.save()
                return redirect('course_success')
        else:
            course_form = TeacherCoursesModelForm()
    else:
        return HttpResponse("You Are Not Teacher....")
    return render(request, 'teachers/teacher_courses.html', {'courses_fm': course_form})


def course_success_add(request):
    return render(request, 'teachers/course_added_success.html')
