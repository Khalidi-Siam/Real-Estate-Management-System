"""
URL configuration for RealEstate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from authentication import views as authentic_view
from authentication.views import signin,password_reset_confirm 

urlpatterns = [
    path('', include('basic.urls')),
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('property/', include('property.urls')),
    path('login/', signin, name='login'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
         name='password_reset'),
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    # Other URL patterns 
    path('agents/', include('Agents.urls')),
    path('payment/', include("Payment.urls")),              
    path('auction/', include('auction.urls')),        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
