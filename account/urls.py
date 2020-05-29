from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token

urlpatterns = [
    # rest_auth login
    path('auth/', include('rest_auth.urls')),
    path('auth/token/refresh/', refresh_jwt_token),
    path('auth/token/verify/', verify_jwt_token),
    path('auth/registration/', include('rest_auth.registration.urls')),
]
