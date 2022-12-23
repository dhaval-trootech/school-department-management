from .models import Courses
from django import forms


class TeacherCoursesModelForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ('course_name', 'standard', 'course_description', 'course_type', 'price', 'user')
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'standard': forms.NumberInput(attrs={'class': 'form-control'}),
            'course_description': forms.Textarea(attrs={'class': 'form-control'}),
            'course_type': forms.RadioSelect(),
            'price': forms.NumberInput(attrs={'class': 'form-control'})

        }

    def __init__(self, *args, **kwargs):
        super(TeacherCoursesModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
