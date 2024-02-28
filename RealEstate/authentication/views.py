from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        

    return render(request, "signup.html")


def signin(request):
    return render(request, "signin.html")