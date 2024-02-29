from . import views
from django.urls import path

urlpatterns = [
    path('signup', views.signup, name = "signup"),
    path('signin', views.signin, name = "signin"),
    path('signout', views.signout, name = "signout"),
    path('profile', views.profile, name = "profile"),
]
