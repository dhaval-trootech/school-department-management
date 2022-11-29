from django import forms
from .models import SchoolUser


class SchoolUserModelForm(forms.ModelForm):
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
                                       error_messages={'required': "please confirm your password."})

    class Meta:
        model = SchoolUser
        fields = ['first_name', 'last_name', 'username', 'email', 'birthdate', 'phone', 'standard', 'subject',
                  'password', 'confirm_password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(attrs={}),
            'phone': forms.NumberInput(attrs={}),
            'standard': forms.NumberInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
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
                'required': "your username is necessary.",
            },
            'password': {
                'required': "please enter the password.",
            },

        }
        help_texts = {
            'username': None,
        }

    def clean(self):
        cleaned_data = super(SchoolUserModelForm, self).clean()
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

    def __init__(self, *args, **kwargs):
        super(SchoolUserModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
