from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Auc_Property)
admin.site.register(Auc_CommercialProperty)
admin.site.register(Auc_ResidentialProperty)
admin.site.register(Auc_LandProperty)
admin.site.register(Bid)