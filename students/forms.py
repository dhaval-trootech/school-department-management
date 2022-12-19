from .models import Courses
from django import forms


class StudentEnrollCourseModelForm(forms.ModelForm):
    class Meta:
        model = Courses
        exclude = ('enroll_time',)
        widgets = {
            'course_name': forms.TextInput(attrs={'readonly': True, 'class': 'partial-disabled', 'value': 'Fronted'}),
            'course_price': forms.TextInput(attrs={'readonly': True, 'class': 'partial-disabled', 'value': 599}),
        }

    def __init__(self, *args, **kwargs):
        super(StudentEnrollCourseModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
