
from django.urls import path
from . import views

urlpatterns = [

    path('add_property', views.add_property, name="add_property"),
    path('add_property_data/<str:property_type>', views.add_property_data, name="add_property_data"),
    path('property_list', views.property_list, name = "property_list"),
    path('property_type', views.property_type, name = "property_type"),

]
