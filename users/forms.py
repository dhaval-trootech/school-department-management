from django import forms
from .models import SchoolUser


class SchoolUserModelForm(forms.ModelForm):
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
                                       error_messages={'required': "please confirm your password."})

    class Meta:
        model = SchoolUser
        fields = ['first_name', 'last_name', 'username', 'user_icon', 'email', 'birthdate', 'phone', 'standard',
                  'subject',
                  'password', 'confirm_password', 'terms_conditions']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'user_icon': forms.FileInput(attrs={}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(attrs={}),
            'phone': forms.NumberInput(attrs={}),
            'standard': forms.NumberInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'local_address': forms.Textarea(attrs={'cols': 30, 'rows': 2}),
            'permanent_address': forms.Textarea(attrs={'cols': 30, 'rows': 2}),
            'terms_conditions': forms.CheckboxInput(attrs={'class': 'form-check-input'})

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
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        return cleaned_data

    def clean_terms_conditions(self):
        val_tc = self.cleaned_data.get('terms_conditions')

        if not val_tc:
            raise forms.ValidationError(
                "You Need to Accept our terms and Agreements"
            )
        return val_tc

    def __init__(self, *args, **kwargs):
        super(SchoolUserModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label


# Login Validation

class SchoolUserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               error_messages={'required': "Your Password Must"},
                               )

    # def clean_password(self):
    #     upass = self.cleaned_data.get("password")
    #
    #     if not SchoolUser.objects.filter(password=upass).exists():
    #         raise forms.ValidationError("You entered wrong Password")
    #     return upass
