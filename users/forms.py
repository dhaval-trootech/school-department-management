from django import forms
from .models import SchoolUser


class SchoolUserModelForm(forms.ModelForm):
    class Meta:
        model = SchoolUser
        fields = ['first_name', 'last_name', 'username', 'email', 'birthdate', 'phone', 'standard', 'subject',
                  'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last Name', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Student mail id', 'class': 'form-control'}),
            'birthdate': forms.DateInput(attrs={'placeholder': 'Enter in YY-MM-DD format'}),
            'phone': forms.NumberInput(attrs={'placeholder': 'Enter without +91 Code'}),
            'standard': forms.NumberInput(attrs={'placeholder': 'Enter your current standard', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Enter your subject', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'enter a strong password', 'class': 'form-control'}),
            'local_address': forms.Textarea(attrs={'cols': 30, 'rows': 2}),
            'permanent_address': forms.Textarea(attrs={'cols': 30, 'rows': 2}),

        }
        error_messages = {
            'first_name': {
                'maxlength': "This writer's name is too long."
            },
            'last_name': {
                'max_length': "This writer's name is too long."
            },
            'username': {
            },
            'standard': {
                'required': "your standard is necessary",
            },
            'password': {
                'required': "please enter the password",
            },

        }
        help_texts = {
            'username': None,
        }

    def __init__(self, *args, **kwargs):
        super(SchoolUserModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
