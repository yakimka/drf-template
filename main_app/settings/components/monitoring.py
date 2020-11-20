from os import environ

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from main_app.settings.components import config
from main_app.settings.components.common import INSTALLED_APPS, MIDDLEWARE

# Prometheus
# https://github.com/korfuri/django-prometheus
ENABLE_PROMETHEUS = config('ENABLE_PROMETHEUS', cast=bool, default=False)
if ENABLE_PROMETHEUS:
    INSTALLED_APPS += (
        'django_prometheus',
    )

    MIDDLEWARE = (
        'django_prometheus.middleware.PrometheusBeforeMiddleware',
        *MIDDLEWARE,
        'django_prometheus.middleware.PrometheusAfterMiddleware'
    )

# Sentry
# https://docs.sentry.io/platforms/python/guides/django/
SENTRY_KEY = config('SENTRY_KEY', None)
SENTRY_ENVIRONMENT = config('SENTRY_ENVIRONMENT', default=environ['DJANGO_ENV'])

if SENTRY_KEY is not None:
    sentry_sdk.init(
        dsn=SENTRY_KEY,
        environment=SENTRY_ENVIRONMENT,
        integrations=[
            DjangoIntegration(),
            # CeleryIntegration(),
            # RedisIntegration(),
        ],

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )
