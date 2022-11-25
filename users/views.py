from django.shortcuts import render
from .forms import SchoolUserModelForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


# Create your views here.

def student_registration(request):
    if request.method == 'POST':
        form = SchoolUserModelForm(request.POST)
        print("i am type of FORM++", type(form))
        if form.is_valid():
            print("FORM CLEANED_DATA++", form.cleaned_data, end='\n\n')
            # Save Data to database
            print("FORM DICT+++", form.__dict__)
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
