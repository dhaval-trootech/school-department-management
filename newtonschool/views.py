from django.shortcuts import render
from school.settings import MEDIA_ROOT


# Create your views here.
def newton_school_dashboard(request):
    return render(request, "newtonschool/dashboard.html", {'media': MEDIA_ROOT})


def newton_school_about(request):
    return render(request, "newtonschool/about.html")
