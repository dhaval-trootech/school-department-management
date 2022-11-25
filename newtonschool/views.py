from django.shortcuts import render


# Create your views here.
def newton_school_dashboard(request):
    return render(request, "newtonschool/dashboard.html")


def newton_school_about(request):
    return render(request, "newtonschool/about.html")
