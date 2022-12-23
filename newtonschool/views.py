from django.shortcuts import render
from teachers.models import Courses
from django.views.generic import ListView


# Create your views here.
def newton_school_dashboard(request):
    return render(request, "newtonschool/dashboard.html", )


def newton_school_about(request):
    return render(request, "newtonschool/about.html")


class CoursesListView(ListView):
    model = Courses
    template_name = 'newtonschool/courses.html'
