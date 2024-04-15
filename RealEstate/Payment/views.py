from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse
import stripe
from django.conf import settings
from .models import *
from authentication.models import UserProfile
from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime
from auction.models import *
from .models import *
from authentication.models import *
stripe.api_key = settings.STRIPE_SECRET_KEY

class CheckoutView(View):
    def get(self, request, property_id):
        try:
            property = Auc_Property.objects.get(pk=property_id)
        except Auc_Property.DoesNotExist:
            # Handle property not found
            return redirect('home')  # Redirect to home page or an error page
        
        return render(request, 'checkout.html', {'property': property})

    def post(self, request, *args, **kwargs):
        property_id = request.POST.get('property_id')
        property = Auc_Property.objects.get(pk=property_id)

        # Create a checkout session with Stripe
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',  # Change to your currency
                        'unit_amount': 2000 * 100,  # Convert price to cents
                        'product_data': {
                            'name': property.Property_Name,
                            # 'images': [property.Property_Pictures.url],  # Access the URL of the image
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            metadata={
                'property_id': property_id,
            },
            success_url=request.build_absolute_uri(reverse('payment_success')+'?property_id=' + str(property.id)),
            cancel_url=request.build_absolute_uri(reverse('payment_cancel')+'?property_id=' + str(property.id)),
        )

        return redirect(checkout_session.url, code=303)

def PaymentSuccessView(request):

    # Get the property and user details based on the request
    property_id = request.GET.get('property_id')  # Example: Property ID passed as a URL parameter
    user_id = request.user.UserProfile
    user_name =  request.user.UserProfile.name
    
    # Query the database to get the property details
    try:
        property = Auc_Property.objects.get(id=property_id)
        property_name = property.Property_Name
        payment = PaymentDetails.objects.create(name = user_name,
                                                property_name = property_name,
                                                payment_time= datetime.now,
                                                payment_amount=2000.00,
                                                property_id = property,
                                                owner_id = user_id
                                                )
        payment.save()

    except Auc_Property.DoesNotExist:
        property_name = "Unknown Property"

    # Get the user's name
    buyer_name = request.user.UserProfile.name
    
    context = {
        'payment_status': 'success',
        'property_name': property_name,
        'buyer_name': buyer_name,
    }
    return render(request, 'confirmation.html', context)

def PaymentCancelView(request):
    property_id = request.GET.get('property_id')  # Example: Property ID passed as a URL parameter
    user_id = request.user.id  # Assuming you're using Django's built-in authentication
    
    try:
        property = Auc_Property.objects.get(id=property_id)
        property_name = property.Property_Name
    except Auc_Property.DoesNotExist:
        property_name = "Unknown Property"

    buyer_name = request.user.UserProfile.name
    
    context = {
        'payment_status': 'cancel',
        'property_name': property_name,
        'buyer_name': buyer_name,
    }
    return render(request, 'confirmation.html', context)

@csrf_exempt
def my_webhook_view(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)
  
  if event['type'] == "checkout.session.completed":
     session = event['data']['object']
     print('ok')

     if session.payment_status == 'paid':
            order_id = session.metadata.get('property_id')
            fulfill_order(order_id)

  return HttpResponse(status=200)

def fulfill_order(order_id):
    order = Auc_Property.objects.get(id=order_id)
    order.Property_Status = 'Sold'
    order.save()