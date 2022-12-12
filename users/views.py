from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SchoolUserModelForm, SchoolUserLoginForm, FormChangePassword, SchoolUserEditForm
from .models import SchoolUser


# Create your views here.

def choose_user(request):
    return render(request, "users/user_choice.html")


def student_registration(request):
    if request.method == 'POST':
        student_reg_form = SchoolUserModelForm(request.POST, request.FILES)
        print("I AM REQUEST POST++ DATA++", request.POST)

        if student_reg_form.is_valid():
            reg = student_reg_form.save(commit=False)
            print("CLEANED DATA +++", student_reg_form.cleaned_data, end='\n\n')
            reg.user_type = 'S'
            reg.set_password(student_reg_form.cleaned_data.get('password'))
            # Final Save Data to database
            reg.save()
            return redirect('user_submit')

    else:
        student_reg_form = SchoolUserModelForm()
    return render(request, "users/student_register.html", {'form': student_reg_form})


def teacher_registration(request):
    if request.method == 'POST':
        teacher_reg_form = SchoolUserModelForm(request.POST, request.FILES)
        if teacher_reg_form.is_valid():
            reg = teacher_reg_form.save(commit=False)
            reg.user_type = 'T'
            reg.set_password(teacher_reg_form.cleaned_data.get('password'))
            # Final Save Data to database
            reg.save()
            return HttpResponseRedirect(reverse('user_submit'))

    else:
        teacher_reg_form = SchoolUserModelForm()
    return render(request, "users/teacher_register.html", {'form': teacher_reg_form})


def thanks_submission(request):
    return render(request, 'users/user_success_submit.html')


def users_login(request):
    if request.method == 'POST':
        user_login_form = SchoolUserLoginForm(request.POST)
        if user_login_form.is_valid():
            uname = user_login_form.cleaned_data.get('username')
            upass = user_login_form.cleaned_data.get('password')
            user = authenticate(username=uname, password=upass)
            print("I am UserAuth++", type(user), type(request.user), end='\n\n')
            if user is not None:
                login(request, user)
                return redirect('school_dashboard')
        else:
            return render(request, 'users/users_login.html', {'form': user_login_form})
    else:
        if request.user.is_authenticated:
            print("Yes I Am Authenticated")
            # return render(request, 'users/user_already_login.html')
            # Send Him/Her Same Dashboard URL....
            return HttpResponseRedirect(reverse('school_dashboard'))

        else:
            user_login_form = SchoolUserLoginForm()
    return render(request, 'users/users_login.html', {'form': user_login_form})


# User Logout
def log_out(request):
    logout(request)
    return redirect('/newtonschool')


# User Password Reset
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user_pass_change_form = FormChangePassword(user=request.user, data=request.POST)
            if user_pass_change_form.is_valid():
                print("DICT++", user_pass_change_form.__dict__)
                user_pass_change_form.save()
                return HttpResponse("Successfully Changed your password")
        else:
            user_pass_change_form = FormChangePassword(user=request.user)
        return render(request, "users/change_password.html", {'form': user_pass_change_form})
    else:
        return HttpResponseRedirect(reverse('users_login'))


def users_dataset(request):
    context = {"dataset": SchoolUser.objects.all()}
    return render(request, "users/users_dataset.html", context)


def user_detail_data(request, ids):
    SchoolUser.objects.get(id=ids).delete()
    return HttpResponseRedirect(reverse('users_dataset'))


def user_profile_edit(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user_edit_form = SchoolUserEditForm(request.POST, request.FILES, instance=request.user)
            if user_edit_form.is_valid():
                user_edit_form.save()
                return HttpResponseRedirect(reverse('school_dashboard'))
        else:
            user_edit_form = SchoolUserEditForm(instance=request.user)
    else:
        return HttpResponseRedirect(reverse('users_login'))
    return render(request, "users/user_profile_edit.html", {'user_edit_fm': user_edit_form})
