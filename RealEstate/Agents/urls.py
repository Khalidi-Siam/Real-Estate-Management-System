# agents/urls.py
from django.urls import path
from .views import agent_dashboard, approve_property

urlpatterns = [
    path('dashboard/', agent_dashboard, name='agent_dashboard'),
    path('approve/<int:property_id>/', approve_property, name='approve_property'),
]
