from django.urls import path
from . import views

urlpatterns = [

    path('checkout/<int:property_id>/', views.CheckoutView.as_view(), name='checkout'),
    path('success/', views.PaymentSuccessView, name='payment_success'),
    path('cancel/', views.PaymentCancelView, name='payment_cancel'),
    path('webhook/stripe', views.my_webhook_view, name='webhook-stripe')
]