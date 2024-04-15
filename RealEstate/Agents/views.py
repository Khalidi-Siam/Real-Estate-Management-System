from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from property.models import AllProperty  
from authentication.models import UserProfile
from .models import *
from django.contrib import messages
from django.urls import reverse


def agent_dashboard(request):
    if request.user.is_authenticated:
        if request.user.UserProfile.is_agent:
            pending_properties = AllProperty.objects.filter(Approval_by_Agent__isnull=True)
            pending_bookings = Booking.objects.filter(agent=request.user.UserProfile, status='pending')
            pending_updates = AllProperty.objects.filter(Approval_by_Agent = request.user.UserProfile, needs_approval = True)
            return render(request, 'agent_dashboard.html', {'pending_properties': pending_properties, 'pending_bookings': pending_bookings, 'pending_updates':pending_updates})
        
        else:
            return redirect("PageNotFound")
    else:
        return redirect(reverse('signin') + '?next=' + request.path)


def approve_property(request, property_id):
    if request.user.is_authenticated:
        if request.user.UserProfile.is_agent:
            if request.method == 'POST':        
                property_instance = get_object_or_404(AllProperty, pk=property_id)
                property_instance.Approval_by_Agent = request.user.UserProfile.name
                property_instance.needs_approval = False
                property_instance.save()
            
            return redirect('agent_dashboard')
        
        else:
            return redirect("PageNotFound")
        
    else:
        return redirect(reverse('signin') + '?next=' + request.path)
        
        
def cancel_approval(request, property_id):
    if request.user.is_authenticated:
        if request.user.UserProfile.is_agent:
            if request.method == 'POST':
                if request.user.UserProfile.is_agent:
                    property_instance = get_object_or_404(AllProperty, pk=property_id)
                    property_instance.Approval_by_Agent = 'Cancel'
                    property_instance.save()

                return redirect('agent_dashboard')
            
        else:
            return redirect("PageNotFound")
            
    else:
        return redirect(reverse('signin') + '?next=' + request.path)
