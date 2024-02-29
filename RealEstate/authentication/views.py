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
                request.session['isLoggedIn'] = True
                return redirect('/')
    
    else:
        form = SignInForm()
    return render(request, "signin.html", {'form': form})

def signout(request):
    logout(request)
    request.session['isLoggedIn'] = False
    next_page = request.GET.get('next', '/')
    return redirect(next_page)


def profile(request):
    user_profile = UserProfile.objects.get(user = request.user)
    profile_fields = get_profile_fields(user_profile)
    return render(request, "profile.html", {'profile_fields':profile_fields})


def get_profile_fields(user_profile):
    fields = [field.name for field in UserProfile._meta.get_fields() if field.name not in ['id', 'user', 'profile_picture']]
    return {field: getattr(user_profile, field, None) for field in fields}
