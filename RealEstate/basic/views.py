from django.shortcuts import render,redirect
from authentication.models import UserProfile
from .models import *
from .forms import *
from django.contrib import messages
from django.core.mail import send_mail
import os
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings  
from django.urls import reverse

# Create your views here.

def about(request):
    return render(request, "about.html")

# def contact(request):
#     return render(request, "contact.html")

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



def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            
            # Send email
            subject = 'Thank you for subscribing!'
            message = 'We appreciate your subscription.'
            from_email = os.environ.get('DB_MAIL')  # Replace with your email
            recipient_list = [email]
            
            send_mail(subject, message, from_email, recipient_list)
            
            form.save()
            return render(request, 'base.html', {'form': SubscribeForm(), 'success': True})
    else:
        form = SubscribeForm()
    return render(request, 'base.html', {'form': form})



def send_email(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Fetching subscribers' email addresses
            subscribers = Subscriber.objects.values_list('email', flat=True)

            # Creating email message
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,  # Use host email from Django settings
                to=subscribers,  # Using subscribers' email addresses
            )

            # Adding attachment if exists
            attachment = request.FILES.get('attachment')
            if attachment:
                email.attach(attachment.name, attachment.read(), attachment.content_type)

            # Sending email
            try:
                email.send()
                return HttpResponse('Email sent successfully!')
            except Exception as e:
                return HttpResponse(f'Failed to send email. Error: {e}')
    else:
        form = SendEmailForm()
    return render(request, 'send_email.html', {'form': form})


def contact(request):
    success_message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message1 = request.POST.get('message')
        message = f"Coustomer mail: {email}\nCoustomer name: {name}\n\n {message1}"
    
        if name and email and subject and message:
            # Send email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # Use your host email as the sender
                [settings.EMAIL_HOST_USER],  # Use your host email as the recipient
                fail_silently=False,
            )
            send_mail(
                "Your Query Submited",
                "Thank You for submitting Query, We will Reach out Soon",
                settings.EMAIL_HOST_USER,  # Use your host email as the sender
                [email],  # Use your host email as the recipient
                fail_silently=False,
            )

            # Save the form data to the database
            Contact.objects.create(name=name, email=email, subject=subject, message=message)
            success_message = "Query submitted successfully. We will contact you soon."
            messages.success(request, success_message)

    return render(request, 'contact.html')
