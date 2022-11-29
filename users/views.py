from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import SchoolUserModelForm


# Create your views here.

def student_registration(request):
    if request.method == 'POST':
        form = SchoolUserModelForm(request.POST)
        if form.is_valid():
            # Save Data to database
            form.save()
            return HttpResponseRedirect(reverse('school_user_logged'))
    else:
        form = SchoolUserModelForm()
    return render(request, "users/student_register.html", {'form': form})


def teacher_registration(request):
    if request.method == 'POST':
        form = SchoolUserModelForm(request.POST)
        if form.is_valid():
            # Save Data to database
            form.save()
            return HttpResponseRedirect(reverse('school_user_logged'))

    else:
        form = SchoolUserModelForm()
    return render(request, "users/teacher_register.html", {'form': form})


def student_login(request):
    form = SchoolUserModelForm()
    return render(request, 'users/student_login.html', {'form': form})


def teacher_login(request):
    form = SchoolUserModelForm()
    return render(request, 'users/teacher_login.html', {'form': form})


def user_logged(request):
    form = SchoolUserModelForm()
    return render(request, 'users/user_logged.html', {'form': form})
