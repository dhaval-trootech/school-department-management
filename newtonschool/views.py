from django.shortcuts import render
from .forms import SchoolModelForm


# Create your views here.

def school_model_form(request):
    context = {}
    # create object of form
    form = SchoolModelForm(request.POST)
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "index.html", context)
