
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from property.models import AllProperty  
from authentication.models import UserProfile
from .models import *

@login_required
def agent_dashboard(request):
    if request.user.UserProfile.is_agent:
        pending_properties = AllProperty.objects.filter(Approval_by_Agent__isnull=True)
        pending_bookings = Booking.objects.filter(agent=request.user.UserProfile, status='pending')
        return render(request, 'agent_dashboard.html', {'pending_properties': pending_properties, 'pending_bookings': pending_bookings})
    else:
        return redirect('signin') 


@login_required
def approve_property(request, property_id):
    if request.method == 'POST':
        if request.user.UserProfile.is_agent:
            property_instance = get_object_or_404(AllProperty, pk=property_id)
            property_instance.Approval_by_Agent = request.user.UserProfile.name
            property_instance.save()
            return redirect('agent_dashboard')
        else:
            return redirect('signin')
          
    else:
        return redirect('agent_dashboard') 
    
@login_required
def cancel_approval(request, property_id):
    if request.method == 'POST':
        if request.user.UserProfile.is_agent:
            property_instance = get_object_or_404(AllProperty, pk=property_id)
            property_instance.Approval_by_Agent = 'Cancel'
            property_instance.save()
        return redirect('agent_dashboard')
