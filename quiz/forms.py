from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    mobileNumber = forms.CharField(required=True, max_length=12, min_length=10,
                               help_text='Required. Please Enter Valid Number')
    tvashId = forms.CharField(required=True, max_length=12, min_length=10, help_text='Required. Tvashta ID')

    class Meta:
        model = User
        fields = ('username','mobileNumber','password1','password2',)

