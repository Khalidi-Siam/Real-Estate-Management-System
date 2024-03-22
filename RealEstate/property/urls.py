
from django.urls import path
from . import views

urlpatterns = [

    path('add_property', views.add_property, name="add_property"),
    path('add_property_data/<str:property_type>', views.add_property_data, name="add_property_data"),
    path('property_list', views.property_list, name = "property_list"),
    path('property_type', views.property_type, name = "property_type"),
    path('property_list/<int:pk>', views.property_detail, name = "property_detail"),
    path('property-calculate/',views.calculate, name = 'calculate'),
    path('posted-properties/', views.posted_properties, name='posted_properties'),
    path('update-property/<int:property_id>/', views.update_property, name='update_property'),
    
]
