
from django.urls import path
from . import views

urlpatterns = [

    path('add_property', views.add_property, name="add_property"),
    path('add_property_data/<str:property_type>', views.add_property_data, name="add_property_data"),
    path('property_list', views.property_list, name = "property_list"),
    path('property_type', views.property_type, name = "property_type"),
    path('property_list/<int:pk>', views.property_detail, name = "property_detail"),
    path('property-calculate/',views.calculate, name = "calculate"),
    path('saved-searches', views.saved_searches, name = "saved_searches"),
    path('apply-saved-search/<int:saved_search_id>/', views.apply_saved_search, name="apply_saved_search"),
    # path('delete-saved-search', views.delete_saved_search, name = "delete_saved_search"),
    path('property/delete-saved-search/<int:saved_search_id>/', views.delete_saved_search, name='delete_saved_search'),

]
