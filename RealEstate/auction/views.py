from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseForbidden
from .forms import *
from property.forms import *
from django.contrib import messages
from authentication.models import UserProfile
from django.urls import reverse
from Payment.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def filtering(request, properties):
    # Create an instance of the form
    filter_form = PropertyFilterForm(request.GET or None)
    # Check if form is submitted and valid
    if filter_form.is_valid():
        # Get cleaned data from the form
        cleaned_data = filter_form.cleaned_data
        property_type = cleaned_data.get('property_type')
        area = cleaned_data.get('area')

        # Filter properties based on form data
        properties = properties.filter(Property_type=property_type) if property_type else properties
        properties = properties.filter(Area=area) if area else properties

        # Additional filters based on property type
        if property_type == 'residential':
            bedrooms = cleaned_data.get('bedrooms')
            bathrooms = cleaned_data.get('bathrooms')

            properties = properties.filter(auc_residentialproperty__Bedrooms=bedrooms) if bedrooms else properties
            properties = properties.filter(auc_residentialproperty__Bathrooms=bathrooms) if bathrooms else properties

        elif property_type == 'commercial':
            business_type = cleaned_data.get('business_type')
            has_conference = cleaned_data.get('has_conference')
            has_security = cleaned_data.get('has_security')

            properties = properties.filter(auc_commercialproperty__Business_type=business_type) if business_type else properties
            properties = properties.filter(auc_commercialproperty__Has_conference_room=True) if has_conference else properties
            properties = properties.filter(auc_commercialproperty__Has_security_system=True) if has_security else properties

        elif property_type == 'land':
            land_type = cleaned_data.get('land_type')

            properties = properties.filter(auc_landproperty__Land_type=land_type) if land_type else properties


        ordering_choice = cleaned_data.get('ordering_choices')
        if ordering_choice == 'price_asc':
            properties = properties.order_by('current_price')
        elif ordering_choice == 'price_desc':
            properties = properties.order_by('-current_price')

    # Pagination
    paginator = Paginator(properties, 3)
    page_number = request.GET.get('page')
    try:
        properties = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        properties = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results
        properties = paginator.page(paginator.num_pages)

    return properties, filter_form

def auction_list(request):

    auctions = Auc_Property.objects.filter(end_time__gt=timezone.now())

    auctions, filter_form = filtering(request, auctions)

    context = {
        'filtered_auctions': auctions,
        'filter_form': filter_form,
    }
    return render(request, 'auction_list.html', context)
    


def auction_detail(request, pk):
    auction = get_object_or_404(Auc_Property, pk=pk)
    if auction.end_time is not None:
        if auction.end_time <= timezone.now():
            # Auction has ended, handle this case as needed
            pass
    bids = auction.bids.all().order_by('amount')
    if auction.bids.exists():
        current_bidder = auction.bids.order_by('amount').first().bidder
    else:
        current_bidder = None
    if request.user.is_authenticated:
        id1 = request.user.UserProfile.id
        property_id =auction.id
        paid = PaymentDetails.objects.filter(owner_id_id = id1, property_id_id = property_id).exists()
    else:
        paid = None
    # print(paid)
    return render(request, 'auction_detail.html', {'auction': auction, 'bids': bids,'current_bidder':current_bidder,'current_time':timezone.now(),'paid': paid })
    

def create_auction(request):
    if request.user.is_authenticated:        
        if request.method == 'POST':
            form = PropertyTypeForm(request.POST)
            if form.is_valid():
                selected_type = form.cleaned_data['Type']
                if selected_type in ['commercial', 'land', 'residential']:                    
                    return redirect('create_auction_data', property_type=selected_type)
                
        else:
            form = PropertyTypeForm()

        return render(request, 'create_auction.html', {'form':form})
    
    else:
        return redirect(reverse('signin') + '?next=' + request.path)
    

def create_auction_data(request, property_type):
    if request.user.is_authenticated:
        if property_type == 'commercial':
            form_class = Auction_CommercialPropertyForm
        elif property_type == 'land':
            form_class = Auction_LandPropertyForm
        elif property_type == 'residential':
            form_class = Auction_ResidentialPropertyForm
        else:
            return redirect('create_auction')

        if request.method == 'POST':
            user_profile = UserProfile.objects.get(user=request.user)
            form = form_class(request.POST, request.FILES)
            
            if form.is_valid():
                property_instance = form.save(commit=False)
                property_instance.seller = user_profile
                property_instance.Property_type = property_type
                property_instance.save()

                messages.success(request, "Property added Successfully. Wait for the approval")
                return redirect('auction_list')

            else:
                messages.error(request, "Something went wrong!")  
        else:
            form = form_class()
        return render(request, 'create_auction_data.html', {'form': form, 'property_type':property_type})

    else:
        return redirect(reverse('signin') + '?next=' + request.path)



def place_bid(request, pk):
    if request.user.is_authenticated:
        auction = get_object_or_404(Auc_Property, pk=pk)

        # Check if the auction has ended
        if auction.end_time <= timezone.now():
            # Auction has ended, handle this case
            if auction.current_price is not None:
                # Determine the winner based on the highest bid
                winning_bid = auction.bids.order_by('-amount').first()
                if winning_bid:
                    auction.winner = winning_bid.bidder
                else:
                    auction.winner = None

                auction.save()
            return redirect('auction_detail', pk=auction.pk)

        if request.method == 'POST':
            # Check if the current user is the seller
            if auction.seller == request.user.UserProfile:
                messages.error(request, "You cannot place a bid on your own auction.")
                return redirect('auction_detail', pk=auction.pk)
            id1 = request.user.UserProfile.id
            property_id =auction.id
            if not PaymentDetails.objects.filter(owner_id_id = id1, property_id_id = property_id).exists():
                return redirect('checkout', pk=auction.pk)
            form = BidForm(request.POST)
            if form.is_valid():
                bid_amount = form.cleaned_data['amount']

                # Ensure bid amount is greater than or equal to current price
                if auction.current_price is None:
                    if bid_amount != auction.start_price:
                        messages.error(request, "The initial bid must be the starting price.")
                        return redirect('auction_detail', pk=auction.pk)
                else:
                    if bid_amount <= auction.current_price or (bid_amount - auction.current_price) % 100 != 0:
                        messages.error(request, "Bid amount must be at least 100 greater than the current price.")
                        return redirect('auction_detail', pk=auction.pk)

                bid = form.save(commit=False)
                bid.bidder = request.user.UserProfile
                bid.auction = auction
                bid.save()

                # Update current price
                auction.current_price = bid_amount
                auction.save()

                messages.success(request, "Bid placed successfully.")
                return redirect('auction_detail', pk=auction.pk)
        else:
            form = BidForm()
        return render(request, 'place_bid.html', {'form': form, 'auction': auction})
    else:
        return redirect(reverse('signin') + '?next=' + request.path)


def view_auction_property_documents(request, property_id):
    if request.user.is_authenticated:
        
        property_instance = get_object_or_404(Auc_Property, pk=property_id)
        property_documents = property_instance.Property_Documents
        
        return render(request, 'view_auction_property_documents.html', {'property_instance': property_instance, 'property_documents': property_documents})
        
        
    else:
        return redirect(reverse('signin') + '?next=' + request.path)
    
def auc_property_detail(request, property_id):
    property_instance = get_object_or_404(Auc_Property, pk=property_id)
    
    if hasattr(property_instance, 'auc_residentialproperty'):
        specific_property_instance = property_instance.auc_residentialproperty
    elif hasattr(property_instance, 'auc_commercialproperty'):
        specific_property_instance = property_instance.auc_commercialproperty
    elif hasattr(property_instance, 'auc_landproperty'):
        specific_property_instance = property_instance.auc_landproperty
    else:
        # Handle the case where the property instance does not belong to any specific type
        specific_property_instance = None


    property_fields = {}
    
    if(specific_property_instance):
        property_fields = vars(specific_property_instance)
        property_fields['Property_Pictures'] = property_instance.Property_Pictures
    print(type(property_fields["start_time"]))
        
    return render(request, 'auc_property_detail.html', {'property_fields':property_fields, 'auc_property.id':property_id})
