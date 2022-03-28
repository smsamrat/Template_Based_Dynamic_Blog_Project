from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('blog'))
    else:
        return HttpResponseRedirect(reverse('signup'))
