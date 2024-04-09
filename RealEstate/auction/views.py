from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseForbidden
from .forms import *
from property.forms import *
from django.contrib import messages
from authentication.models import UserProfile
from django.urls import reverse



def auction_list(request):
    if request.user.is_authenticated:
        auctions = Auc_Property.objects.filter(end_time__gt=timezone.now())
        return render(request, 'auction_list.html', {'auctions': auctions})
    
    else:
        return redirect(reverse('signin') + '?next=' + request.path)


def auction_detail(request, pk):
    if request.user.is_authenticated:
      auction = get_object_or_404(Auc_Property, pk=pk)
      if auction.end_time <= timezone.now():
          # Auction has ended, handle this case as needed
          pass
      bids = auction.bids.all().order_by('-amount')
      if auction.bids.exists():
          current_bidder = auction.bids.order_by('amount').first().bidder
      else:
          current_bidder = None
      return render(request, 'auction_detail.html', {'auction': auction, 'bids': bids,'current_bidder':current_bidder,'current_time':timezone.now()})
    else:
        return redirect(reverse('signin') + '?next=' + request.path)

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
            # For example, determine the winner and update the auction status
            if auction.current_price.exists():
                # Determine the winner based on the highest bid
                winning_bid = auction.bids.order_by('amount').first()
                auction.winner = winning_bid.bidder
            else:
                # No bids were placed, handle this case by setting the winner to None
                auction.winner = None

            auction.save()
            return redirect('auction_detail', pk=auction.pk)

        if request.method == 'POST':
            # Check if the current user is the seller
            if auction.seller == request.user.UserProfile:
                messages.error(request, "You cannot place a bid on your own auction.")
                return redirect('auction_detail', pk=auction.pk)

            form = BidForm(request.POST)
            if form.is_valid():
                bid_amount = form.cleaned_data['amount']

                # Ensure bid amount is greater than or equal to start price
                if not auction.bids.exists() and bid_amount < auction.start_price:
                    messages.error(request, "Bid amount cannot be less than the starting price.")
                    return redirect('auction_detail', pk=auction.pk)

                if bid_amount > 0 and bid_amount % 100 == 0:
                    bid = form.save(commit=False)
                    bid.bidder = request.user.UserProfile  # Assuming UserProfile is related to User
                    bid.auction = auction
                    bid.save()

                    # If no bids were placed before, set current price to start price
                    if not auction.bids.exists():
                        auction.current_price = auction.start_price

                    auction.current_price += bid_amount  # Add bid amount to current price
                    auction.save()

                    messages.success(request, "Bid placed successfully.")
                    return redirect('auction_detail', pk=auction.pk)
                else:
                    messages.error(request, "Bid amount must be a positive multiple of 100.")
        else:
            form = BidForm()
        return render(request, 'place_bid.html', {'form': form, 'auction': auction})
   else:
        return redirect(reverse('signin') + '?next=' + request.path)

