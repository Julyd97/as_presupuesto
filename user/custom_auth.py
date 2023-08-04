from datetime import datetime
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import BlacklistedRefreshToken

class BlacklistJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        if user_auth_tuple is None:
            return None

        user, _ = user_auth_tuple
        if self.is_token_blacklisted(request):
            return None

        return user, None

    def is_token_blacklisted(self, request):
        token = self.get_raw_token(request)
        return BlacklistedRefreshToken.objects.filter(token=token).exists()