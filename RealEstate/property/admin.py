from django.contrib import admin
from .models import AllProperty, CommercialProperty, LandProperty, ResidentialProperty
# Register your models here.
admin.site.register(AllProperty)
admin.site.register(CommercialProperty)
admin.site.register(LandProperty)
admin.site.register(ResidentialProperty)