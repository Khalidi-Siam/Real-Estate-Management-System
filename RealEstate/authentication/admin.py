from django.contrib import admin
from .models import UserProfile

# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'admin']  # Define fields to display in the admin list view
#     list_editable = ['admin']  # Make the 'admin' field editable in the admin list view

#     def get_fields(self, request, obj=None):
#         fields = super().get_fields(request, obj)
#         if not request.user.is_superuser:
#             fields.remove('admin')  # Remove the 'admin' field if the user is not a superuser
#         return fields

# admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(UserProfile)
