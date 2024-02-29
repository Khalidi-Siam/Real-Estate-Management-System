from authentication.models import UserProfile

def get_user_name(request):
    name = ""
    is_logged_in = request.session.get('isLoggedIn', False)
    if is_logged_in:
        user_profile = UserProfile.objects.get(user = request.user)
        name = user_profile.name
        
    return {'is_logged_in': is_logged_in, 'name' : name}