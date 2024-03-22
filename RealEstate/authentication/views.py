from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm, SignInForm, EditProfileForm
from .models import UserProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.urls import reverse

# Create your views here.
User = get_user_model()

def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been reset sucessfully.")
                # Redirect to reset confirmation page after password reset
                return redirect('login')
        else:
            form = SetPasswordForm(user)
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "The password reset link is invalid")
        return redirect('password_reset')
    
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

            messages.success(request, "Registration successful. Please sign in.")
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
                messages.success(request, "Successfully Signed in")
                next_url = request.GET.get('next')
                if next_url:
                    if(next_url == "/authentication/signup"):
                        return redirect("/")
                    else:
                        return redirect(next_url)
                else:
                    return redirect("/")
    
    else:        
        form = SignInForm()
    
    return render(request, "signin.html", {'form': form})

@login_required
def signout(request):
    logout(request)
    request.session['isLoggedIn'] = False
    next_page = request.GET.get('next', '/')
    messages.success(request, "Successfully Signed Out")
    return redirect(next_page)

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user = request.user)
    profile_fields = get_profile_fields(user_profile)
    profile_fields['profile_picture'] = user_profile.profile_picture
    return render(request, "profile.html", {'profile_fields':profile_fields})


def get_profile_fields(user_profile):
    fields = [field.name for field in UserProfile._meta.get_fields() if field.name not in ['id', 'user', 'profile_picture', 'properties', 'reviews']]
    return {field: getattr(user_profile, field, None) for field in fields}

@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user = request.user)

    if request.method == 'POST':    
        form = EditProfileForm(request.POST, request.FILES, instance = user_profile)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.username = form.cleaned_data['email']
            request.user.save()

            form.save()
            return redirect('profile')
        
    else:
        form = EditProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form':form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        messages.success(request, "Account deleted successfully")
        return redirect('/')
    
    else:
        return redirect('profile')