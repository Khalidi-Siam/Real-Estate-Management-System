from django.shortcuts import render, redirect
from .models import AllProperty, UserProfile
from .forms import *
from django.contrib import messages
from django.db.models import Q


def add_property(request):
    if request.session.get('isLoggedIn', False):
        if request.method == 'POST':
            selected_type = request.POST.get('Type')
            if selected_type in ['commercial', 'land', 'residential']:
                
                return redirect('add_property_data', property_type=selected_type)

        return render(request, 'add_property.html')

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

    if(specific_property_instance):
        property_fields = vars(specific_property_instance)
        property_fields['Property_Pictures'] = property_instance.Property_Pictures

    else:
        property_fields = {}

    all_review = Reviews.objects.filter(property = property_instance)

    if request.method == "POST":
        if request.user.is_authenticated:
            user_review = Reviews.objects.filter(property = property_instance, user = request.user.UserProfile).first()
            if str(property_instance.user.email) == str(request.user): #condition check sothat property owner couldn't review his own property
                messages.error(request, "You can't review your own property.")
                return redirect('property_detail', pk = pk)
            elif user_review: #condtion check whether user already reviewed the specific property. one review per property allowed
                messages.error(request, "You have already reviewed this property.")
                return redirect('property_detail', pk = pk)
            else:
                form = ReviewForm(request.POST)
                if form.is_valid():
                    review = form.save(commit=False)
                    review.user = request.user.UserProfile
                    review.property = property_instance

                    review.save()
                    return redirect('property_detail', pk = pk)
            
        else:
            return redirect('signin')
        
    else:
        form = ReviewForm()

    return render(request, "property_detail.html", {'property_fields':property_fields, 'form':form, 'all_review':all_review})



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
    return render(request, "Calculate.html")