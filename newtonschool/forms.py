from django.forms import ModelForm
from .models import School


class SchoolModelForm(ModelForm):
    class Meta:
        model = School
        fields = "__all__"
