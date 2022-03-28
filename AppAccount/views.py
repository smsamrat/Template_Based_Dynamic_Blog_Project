from urllib import request
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse  
from .forms import SignUpForm,UpdateProfile,AddProfilePicture
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm

# Create your views here.
def auth_signup(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    context ={
        'form':form
    }
    return render(request,'app_account/signup.html',context)

def auth_login(request):
    form =AuthenticationForm()
    if request.method == "POST":
        form =AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
            return HttpResponseRedirect(reverse('index')) 
    return render(request,'app_account/login.html',context={'form':form})

@login_required
def auth_logout(request):
	logout(request)
	return redirect("login")

@login_required
def user_Profile(request):
    return render(request,'app_account/user_Profile.html',context={})

@login_required
def edit_profile(request):
    form = UpdateProfile(instance = request.user)
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
        # form = UpdateProfile(instance = request.user)
        return redirect('user_Profile')
    return render(request,'app_account/edit_profile.html',context={'form':form})

@login_required
def edit_password(request):
    form = PasswordChangeForm(request.user)
    if request.method=='POST':
        form = PasswordChangeForm( request.user,request.POST)
        if form.is_valid():
            form.save()
    return render(request,'app_account/edit_password.html',context={'form':form})

@login_required
def add_profile_picture(request):
    # current_user = request.user
    form = AddProfilePicture()
    if request.method=='POST':
        form = AddProfilePicture(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            form.save()
            return redirect('user_Profile')
    return render(request,'app_account/add_profile_pic.html',context={'form':form})

@login_required
def edit_profile_picture(request):
    current_user = request.user
    form = AddProfilePicture(instance = current_user.user_profiles)
    if request.method=='POST':
        form = AddProfilePicture(request.POST,request.FILES, instance = current_user.user_profiles)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            form.save()
        return redirect('user_Profile')
    return render(request,'app_account/edit_profile_picture.html',context={'form':form})