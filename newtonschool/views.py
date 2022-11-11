from django.shortcuts import render
from .forms import SchoolModelForm
from django.http import HttpResponse


# Create your views here.

# Method - 1
def school_model_form(request):
    school_form = SchoolModelForm()
    context = {'form': school_form}
    if request.method == 'POST':
        form = SchoolModelForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return HttpResponse("data submitted successfully")
    return render(request, "newtonschool/school_form.html", context)


# Method - 2
# def school_model_form(request):
#     form = SchoolModelForm()
#     context = {'form': form}
#     if request.method == 'POST':
#         print("Before IS_VALID>:", request.POST)
#         form.established_year = 999
#         form.owner_name = request.POST['owner_name']
#         form.rating = request.POST['rating']
#         data = form.save(commit=False)
#         # Finally write the changes into database
#         data.save()
#         return HttpResponse("data submitted successfully")
#     return render(request, "newtonschool/school_form.html", context)
