from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserProfileFrom
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'solarpv/index.html')

def dashboard(request):
    return render(request, 'solarpv/dashboard.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if request.user.is_staff:
                return redirect('/admin/')
            else:
                return redirect('/')

    else:
        form = AuthenticationForm()
    return render(request,'solarpv/login.html', {'form' : form})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileFrom(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.users = user

            profile.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()
        profile_form = UserProfileFrom()

    return render(request, 'solarpv/register.html', {'form' : form, 'profile_form' : profile_form})
