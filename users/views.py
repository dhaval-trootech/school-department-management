from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import SchoolUserModelForm, SchoolUserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


# Create your views here.

def choose_user(request):
    return render(request, "users/user_choice.html")


def student_registration(request):
    if request.method == 'POST':
        form = SchoolUserModelForm(request.POST)

        if form.is_valid():
            reg = form.save(commit=False)

            reg.user_type = 'S'
            reg.set_password(form.cleaned_data.get('password'))
            # Final Save Data to database
            reg.save()
            return redirect('/users/login')
    else:
        if request.user.is_authenticated:
            print("Yes I Am Authenicated")
            return HttpResponse('YOU ARE ALREADY LOGIN, REGISTRATION NOT FOR YOU....')
        else:
            print("you are not AUthnicated")
            form = SchoolUserModelForm()
    return render(request, "users/student_register.html", {'form': form})


def teacher_registration(request):
    if request.method == 'POST':
        form = SchoolUserModelForm(request.POST)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.user_type = 'T'
            reg.set_password(form.cleaned_data.get('password'))
            # Final Save Data to database
            reg.save()
            return HttpResponseRedirect(reverse('users_login'))

    else:
        form = SchoolUserModelForm()
    return render(request, "users/teacher_register.html", {'form': form})


def users_login(request):
    if request.method == 'POST':
        fm = SchoolUserLoginForm(request.POST)
        if fm.is_valid():
            print("I AM VALIDATED++", fm.cleaned_data)
            uname = fm.cleaned_data.get('username')
            upass = fm.cleaned_data.get('password')
            user = authenticate(username=uname, password=upass)
            print("I am UserAuth++", type(user), type(request.user))
            # print("I am UserAuth 2++", request.user.local_address)
            if user is not None:
                login(request, user)
                return redirect('/newtonschool')
        else:
            return render(request, 'users/users_login.html', {'form': fm})
    else:
        fm = SchoolUserLoginForm()
    return render(request, 'users/users_login.html', {'form': fm})


def log_out(request):
    logout(request)
    return redirect('/newtonschool')
