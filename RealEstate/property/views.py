from django.shortcuts import render, redirect
from .models import AllProperty, CommercialProperty, LandProperty, ResidentialProperty
from .forms import PropertyForm, LandPropertyForm, CommercialPropertyForm, ResidentialPropertyForm
from django.urls import reverse


# Create your views here.

def add_property(request):
    if request.session.get('isLoggedIn', False):
            if request.method == 'POST':
                selected_type = request.POST.get('Type')
                if selected_type == 'commercial':
                    return redirect('add-commercial-property')
                elif selected_type == 'land':
                    return redirect('add-land-property')
                elif selected_type == 'residential':
                    return redirect('add-residential-property')
            return render(request, 'add_Property.html')

    else:
        return redirect('signin')

def add_commercial_property(request):
    if request.method == 'POST':
        form = CommercialPropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property-list')  # Change to your property list URL
    else:
        form = CommercialPropertyForm()
    return render(request, 'add_commercial_property.html', {'form': form})

def add_land_property(request):
    if request.method == 'POST':
        form = LandPropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property-list')  # Change to your property list URL
    else:
        form = LandPropertyForm()
    return render(request, 'add_land_property.html', {'form': form})

def add_residential_property(request):
    if request.method == 'POST':
        form = ResidentialPropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property-list')  # Change to your property list URL
    else:
        form = ResidentialPropertyForm()
    return render(request, 'add_residential_property.html', {'form': form})

# def update_property(request, property_id):
#     property_instance = AllProperty.objects.get(pk=property_id)
#     if request.method == 'POST':
#         form = PropertyForm(request.POST, request.FILES, instance=property_instance)
#         if form.is_valid():
#             form.save()
#             return redirect('property_list')  # Redirect to a view that lists all properties
#     else:
#         form = PropertyForm(instance=property_instance)
#     return render(request, 'update_property.html', {'form': form})

def property_list(request):
    residential_property = ResidentialProperty.objects.all()
    commercial_property = CommercialProperty.objects.all()
    land_property = LandProperty.objects.all()
    total_list = {'residential_property': residential_property, 
                'commercial_property': commercial_property,
                'land_property': land_property
                }

    return render(request, "property_list.html", total_list)

def property_type(request):
    return render(request, "property_type.html")
