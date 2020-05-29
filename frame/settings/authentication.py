AUTHENTICATION_APPS = [
    # rest auth
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',

    # django allauth apps
    'allauth',
    'allauth.account',
]

SITE_ID = 1

# Username settings override
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'uid'

# Default rest-auth user detail serializer
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'account.serializers.UserSerializer'
}

# Email login
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

# Registration with email, instead of username
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# JET Enable
REST_USE_JWT = True

JWT_AUTH = {
    'JWT_PAYLOAD_HANDLER': 'account.utils.jwt_payload_handler',
    'JWT_ALLOW_REFRESH': True,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}
