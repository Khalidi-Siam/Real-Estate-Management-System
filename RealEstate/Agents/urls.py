# agents/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', agent_dashboard, name='agent_dashboard'),
    path('approve/<int:property_id>/', approve_property, name='approve_property'),
    path('cancel_approval/<int:property_id>/', cancel_approval, name='cancel_approval'),
]
