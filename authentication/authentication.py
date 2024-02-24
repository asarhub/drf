from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from authentication.models import User
from django.conf import settings

class ThirdPartyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        if request.headers.get('Authorization') == settings.THIRD_PARTY_TOKEN:
            third_party_dummy_user = User(
                username="thirdpartyuser",
                is_superuser=True,
                is_active=True
            )
            return (third_party_dummy_user, None)#(request.user, request.auth)
        else:
            return None