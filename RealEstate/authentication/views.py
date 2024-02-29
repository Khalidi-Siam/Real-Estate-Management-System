from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm, SignInForm
from .models import UserProfile
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']


            user = User.objects.create_user(username=email, email = email, password = password)

            user_profile = UserProfile.objects.create(name = name, email = email)
            user_profile.user = user
            user_profile.save()


            return redirect('signin')
    
    else:
        form = SignUpForm()

    return render(request, "signup.html", {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
    
    else:
        form = SignInForm()
    return render(request, "signin.html", {'form': form})

def signout(request):
    logout(request)
    return redirect('/')