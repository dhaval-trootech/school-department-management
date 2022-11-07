from django.shortcuts import render


# Create your views here.

def teacher_register(request):
    return render(request, 'teachers/teacher_reg.html')


def teacher_login(request):
    return render(request, 'teachers/teacher_log.html')
