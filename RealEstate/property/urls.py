from . import views
from django.urls import path

urlpatterns = [
    path('add_property', views.add_property, name = "add_property"),
    path('add_commercial_property', views.add_commercial_property, name = "add_commercial_property"),
    path('add_land_property', views.add_land_property, name = "add_land_property"),
    path('add_residential_property', views.add_residential_property, name = "add_residential_property"),
    path('property_list', views.property_list, name = "property_list"),
    path('property_type', views.property_type, name = "property_type"),
]
