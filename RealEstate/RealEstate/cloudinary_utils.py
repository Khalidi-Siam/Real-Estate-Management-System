"""
Custom upload functions for Cloudinary storage with organized folder structure
"""
import os
from django.utils.deconstruct import deconstructible


@deconstructible
class CloudinaryUploadTo:
    """
    Custom upload path generator for Cloudinary
    Creates organized folder structure: media/folder_name/
    """
    
    def __init__(self, folder_name):
        self.folder_name = folder_name
    
    def __call__(self, instance, filename):
        # Get file extension
        ext = filename.split('.')[-1]
        
        # Create organized path: media/folder_name/filename
        return f'media/{self.folder_name}/{filename}'


# Pre-defined upload functions for different file types
def profile_picture_upload_to(instance, filename):
    """Upload path for profile pictures: media/profile_picture/"""
    return f'media/profile_picture/{filename}'


def property_pictures_upload_to(instance, filename):
    """Upload path for property pictures: media/property_pictures/"""
    return f'media/property_pictures/{filename}'


def property_documents_upload_to(instance, filename):
    """Upload path for property documents: media/property_documents/"""
    return f'media/property_documents/{filename}'


def auction_pictures_upload_to(instance, filename):
    """Upload path for auction pictures: media/auction_pictures/"""
    return f'media/auction_pictures/{filename}'


def auction_documents_upload_to(instance, filename):
    """Upload path for auction documents: media/auction_documents/"""
    return f'media/auction_documents/{filename}'