from pyexpat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import Commnet

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commnet
        fields = ('comment_text',)