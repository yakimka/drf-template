# Django REST framework
# https://github.com/encode/django-rest-framework

REST_FRAMEWORK = {
    # If you need django.auth support:
    # delete this 3 lines and uncomment DEFAULT_PERMISSION_CLASSES, DEFAULT_AUTHENTICATION_CLASSES
    'DEFAULT_PERMISSION_CLASSES': [],
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'UNAUTHENTICATED_USER': None,
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.AllowAny'
    # ],
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'authtoken.utils.AuthTokenAuthentication',
    #     'authtoken.utils.AuthUserApiKeyAuthentication',
    # ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ['v1'],
    'COERCE_DECIMAL_TO_STRING': True,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}
