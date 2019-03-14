from django.contrib.auth.backends import ModelBackend
from data.users import User

class NewCustomAuthBackend(ModelBackend):
    """Logs in user with email and password."""

    def authenticate(email=None, password=None):
        try:
            return User.objects.get(email=email, password=password)
        except User.DoesNotExist:
            return None
    
    # get a user object
    def get_user(_id):
        try:
            return User.objects.get(pk=_id)
        except User.DoesNotExist:
            return None
