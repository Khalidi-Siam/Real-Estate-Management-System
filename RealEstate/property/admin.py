from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(AllProperty)
admin.site.register(LandProperty)
admin.site.register(CommercialProperty)
admin.site.register(ResidentialProperty)