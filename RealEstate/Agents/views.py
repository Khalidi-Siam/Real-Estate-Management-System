# agents/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from property.models import AllProperty  # Assuming your property model is in 'property' app
from authentication.models import UserProfile
@login_required
def agent_dashboard(request):
    if request.user.UserProfile.is_agent:
        pending_properties = AllProperty.objects.filter(Approval_by_Agent__isnull=True)
        return render(request, 'agent_dashboard.html', {'pending_properties': pending_properties})
    else:
        return redirect('signin')  # Redirect to signin page if user is not an agent

@login_required
def approve_property(request, property_id):
    if request.user.UserProfile.is_agent:
        property_instance = AllProperty.objects.get(pk=property_id)
        property_instance.Approval_by_Agent = request.user.UserProfile.name
        property_instance.save()
        return redirect('agent_dashboard')
    else:
        return redirect('signin')  # Redirect to signin page if user is not an agent
