from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Reviews)
admin.site.register(Subscriber)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact_no', 'gender', 'nid', 'dob', 'address', 'is_agent')
    list_editable = ('is_agent',)

admin.site.unregister(UserProfile)  # Unregister existing registration
admin.site.register(UserProfile, UserProfileAdmin)