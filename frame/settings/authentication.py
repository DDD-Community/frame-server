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

# Email login
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

# Registration with email, instead of username
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)
