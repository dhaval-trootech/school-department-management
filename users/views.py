from django.shortcuts import render
from .forms import SchoolUserModelForm
from django.http import HttpResponse


# Create your views here.
def school_user_registration(request):
    if request.method == 'POST':
        form = SchoolUserModelForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            # Final Save Data to database
            data.save()
            print("M Form DICT METHOD++", form.__dict__)
            return HttpResponse("school user registration successfully")
    else:
        form = SchoolUserModelForm()
    return render(request, "users/school_user_reg.html", {'form': form})
