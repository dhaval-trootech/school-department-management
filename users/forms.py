from django import forms
from .models import SchoolUser


class SchoolUserModelForm(forms.ModelForm):
    class Meta:
        model = SchoolUser
        fields = ['first_name', 'last_name', 'username', 'birthdate', 'phone', 'standard', 'subject',
                  'local_address', 'permanent_address', 'user_type']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
