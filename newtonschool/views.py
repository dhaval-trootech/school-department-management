from django.shortcuts import render
from .forms import SchoolModelForm
from django.http import HttpResponse


# Create your views here.

# Method - 1
def school_model_form(request):
    if request.method == 'POST':
        form = SchoolModelForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.owner_name = "MR. S NARAYAN"
            # Final Save Data to database
            data.save()
            return HttpResponse("data submitted successfully")
    else:
        form = SchoolModelForm()
    return render(request, "newtonschool/school_form.html", {'form': form})
