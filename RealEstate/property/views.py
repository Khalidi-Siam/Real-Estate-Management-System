from django.shortcuts import render, redirect
from .models import AllProperty, UserProfile
from .forms import *
from django.contrib import messages
from django.db.models import Q


def add_property(request):
    if request.session.get('isLoggedIn', False):
        
        if request.method == 'POST':
            form = PropertyTypeForm(request.POST)
            if form.is_valid():
                selected_type = form.cleaned_data['Type']
                if selected_type in ['commercial', 'land', 'residential']:                    
                    return redirect('add_property_data', property_type=selected_type)
                
        else:
            form = PropertyTypeForm()

        return render(request, 'add_property.html', {'form':form})

    else:
        return redirect('signin')

def add_property_data(request, property_type):
    if property_type == 'commercial':
        form_class = CommercialPropertyForm
    elif property_type == 'land':
        form_class = LandPropertyForm
    elif property_type == 'residential':
        form_class = ResidentialPropertyForm
    else:
        return redirect('add_property')

    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)
        form = form_class(request.POST, request.FILES)
        
        if form.is_valid():
            property_instance = form.save(commit=False)
            property_instance.user = user_profile
            property_instance.Property_type = property_type
            property_instance.save()

            messages.success(request, "Property added Successfully")
            return redirect('property_list')

        else:
            messages.error(request, "Something went wrong!")  
    else:
        form = form_class()
    return render(request, 'add_property_data.html', {'form': form, 'property_type':property_type})


def update_property(request, property_id):
    property_instance = AllProperty.objects.get(pk=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Property updated Successfully")
            return redirect('property_list')  
        
    else:
        form = PropertyForm(instance=property_instance)
        
    return render(request, 'update_property.html', {'form': form})

def property_detail(request, pk):
    property_instance = AllProperty.objects.get(pk = pk)
    
    if hasattr(property_instance, 'residentialproperty'):
        specific_property_instance = property_instance.residentialproperty
    elif hasattr(property_instance, 'commercialproperty'):
        specific_property_instance = property_instance.commercialproperty
    elif hasattr(property_instance, 'landproperty'):
        specific_property_instance = property_instance.landproperty
    else:
        # Handle the case where the property instance does not belong to any specific type
        specific_property_instance = None


    property_fields = {}
    
    if(specific_property_instance):
        property_fields = vars(specific_property_instance)
        property_fields['Property_Pictures'] = property_instance.Property_Pictures


    return render(request, "property_detail.html", {'property_fields':property_fields})



def property_list(request):
    # total_list = AllProperty.objects.all()
    

    total_list = AllProperty.objects.filter(
        Q(residentialproperty__isnull=False) | 
        Q(commercialproperty__isnull=False) |
        Q(landproperty__isnull=False)
    ).select_related('residentialproperty', 'commercialproperty', 'landproperty')
    return render(request, "property_list.html", {'total_list': total_list})



def property_type(request):
    return render(request, "property_type.html")


def calculate(request):
    if request.method == 'POST':
        form = PropertyCalculatorForm(request.POST)
        if form.is_valid():
            per_sqft_price = form.cleaned_data['per_sqft_price']
            total_sqft = form.cleaned_data['total_sqft']
            parking_sqft = form.cleaned_data['parking_sqft']
            parking_price_per_sqft = form.cleaned_data['parking_price_per_sqft']
            
            total_amount = (per_sqft_price * total_sqft) + (parking_sqft * parking_price_per_sqft)
            
            return render(request, 'Calculate.html', {'form': form, 'total_amount': total_amount})
    else:
        form = PropertyCalculatorForm()

    return render(request, 'Calculate.html', {'form': form})