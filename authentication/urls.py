from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include
from authentication.views import sign_up_view

urlpatterns = [
    path('sign-up/', sign_up_view.as_view(), name="sign_up"),
    path('sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
