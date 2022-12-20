from .models import Courses
from django import forms
from django.forms import ValidationError


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

    def clean_course_confirmation(self):
        val_course_confirmation = self.cleaned_data.get('course_confirmation')
        if not val_course_confirmation:
            raise ValidationError(
                "Please confirm your order to process further."
            )
        return val_course_confirmation
