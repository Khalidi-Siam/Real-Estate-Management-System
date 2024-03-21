from django.shortcuts import render,redirect
from authentication.models import UserProfile
from .models import *
from .forms import *
from django.contrib import messages
from django.urls import reverse
# Create your views here.

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def faqs(request):
    return render(request, "faqs.html")

def license(request):
    return render(request, "license.html")

def terms(request):
    return render(request, "terms.html")

def testimonial(request):
    all_review = Reviews.objects.all()

    if request.method == "POST":
        if request.user.is_authenticated:
            user_review = Reviews.objects.filter(user = request.user.UserProfile).first()

            if user_review: #condtion check whether user already reviewed the specific property. one review per property allowed
                messages.error(request, "You have already give your feedback")
                return redirect('testimonial')
            else:
                form = ReviewForm(request.POST)
                if form.is_valid():
                    review = form.save(commit=False)
                    review.user = request.user.UserProfile
                    review.save()
                    messages.success(request, "Reviewed successfully")
                    return redirect('testimonial')
        
        else:
            return redirect(reverse('signin') + '?next=' + request.path)
        
    else:
        form = ReviewForm()

    return render(request, "testimonial.html", {'all_review':all_review, 'form':form})

def home(request):
    top_review = Reviews.objects.order_by('-rating')[:3]
    return render(request, "index.html", {'top_review':top_review})

def notFound(request):
    return render(request, "404.html")