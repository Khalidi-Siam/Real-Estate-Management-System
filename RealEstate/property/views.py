
from django.shortcuts import render, redirect
from .models import AllProperty, CommercialProperty, LandProperty, ResidentialProperty,UserProfile
from .forms import PropertyForm, LandPropertyForm, CommercialPropertyForm, ResidentialPropertyForm


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

            return redirect('property_list')  
    else:
        form = form_class()
    return render(request, 'add_property_data.html', {'form': form, 'property_type':property_type})


def update_property(request, property_id):
    property_instance = AllProperty.objects.get(pk=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_instance)
        if form.is_valid():
            form.save()
            return redirect('property_list')  
    else:

        form = PropertyForm(instance=property_instance)
    return render(request, 'update_property.html', {'form': form})

def property_detail(request, pk):
    property_instance = AllProperty.objects.get(pk = pk)
    property_fields = get_property_fields(property_instance)
    property_fields['Property_Pictures'] = property_instance.Property_Pictures
    print(property_fields)

    return render(request, "property_detail.html", {'property_fields':property_fields})

def get_property_fields(property):
    fields = [field.name for field in AllProperty._meta.get_fields() if field.name not in ['id', 'user', 'Property_Pictures', 'residentialproperty','commercialproperty', 'landproperty']]
    return {field: getattr(property, field, None) for field in fields}


def property_list(request):
    total_list = AllProperty.objects.all()
    return render(request, "property_list.html", {'total_list': total_list})



def property_type(request):
    return render(request, "property_type.html")

def calculate(request):
    return render(request, "Calculate.html")