from django.shortcuts import render

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
    return render(request, "testimonial.html")

def home(request):
    return render(request, "index.html")