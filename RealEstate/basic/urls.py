from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('about', views.about, name = "about"),
    path('faqs', views.faqs, name = "faqs"),
    path('license', views.license, name = "license"),
    path('terms', views.terms, name = "terms"),
    path('testimonial', views.testimonial, name = "testimonial"),
    path('page-not-found', views.notFound, name = "PageNotFound"),
    path('subscribe', views.subscribe, name="subscribe"),
    path('send-email/', views.send_email, name='send_email'),
    path('contact/', views.contact, name='contact'),

        
]
