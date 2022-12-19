from django.shortcuts import render
from teachers.models import Courses
from django.views.generic import TemplateView
from django.views import View


# Create your views here.
def newton_school_dashboard(request):
    return render(request, "newtonschool/dashboard.html", )


def newton_school_about(request):
    return render(request, "newtonschool/about.html")


# def newton_school_courses(request):
#     course_db = Courses.objects.all()
#     return render(request, 'newtonschool/courses.html', {'courses': course_db})


class CoursesClassBasedView(TemplateView):
    template_name = 'newtonschool/courses.html'

    def get(self, request):
        course_db = Courses.objects.all()
        return render(request, self.template_name, {'courses': course_db})
