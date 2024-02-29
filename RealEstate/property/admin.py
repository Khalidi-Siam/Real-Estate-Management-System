from django.contrib import admin
from .models import Allproperty,LandProperty,CommercialProperty,ResidentialProperty
# Register your models here.
admin.site.register(Allproperty)
admin.site.register(LandProperty)
admin.site.register(CommercialProperty)
admin.site.register(ResidentialProperty)