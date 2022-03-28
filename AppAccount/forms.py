from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import UserProfiles

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email address', required=True)
    class Meta:
        model = User
        fields=('username','email','password1','password2',)

class UpdateProfile(UserChangeForm):
    class Meta:
        model = User
        fields=('username','email','first_name','last_name')

class AddProfilePicture(forms.ModelForm):
    class Meta:
        model = UserProfiles
        fields=('images',)

