from django import forms
from .models import School


class SchoolModelForm(forms.ModelForm):

    class Meta:
        model = School
        fields = ['city', 'established_year', 'rating', 'owner_name']
    city = forms.CharField(label="Name Your City")
