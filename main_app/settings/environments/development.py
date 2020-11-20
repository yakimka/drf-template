"""
This file contains all the settings that defines the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""

import logging
from typing import List

from main_app.settings.components.common import INSTALLED_APPS, MIDDLEWARE

# Setting the development status:

DEBUG = True

# Installed apps for developement only:

INSTALLED_APPS += (
    'nplusone.ext.django',
    'extra_checks',
    'silk',
)

# Static files:
# https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-STATICFILES_DIRS

STATICFILES_DIRS: List[str] = []

# nplusone
# https://github.com/jmcarp/nplusone

# Should be the first in line:
MIDDLEWARE = ('nplusone.ext.django.NPlusOneMiddleware', *MIDDLEWARE)

# Logging N+1 requests:
# NPLUSONE_RAISE = True  # comment out if you want to allow N+1 requests
NPLUSONE_LOGGER = logging.getLogger('django')
NPLUSONE_LOG_LEVEL = logging.WARN
NPLUSONE_WHITELIST = [
    {'model': 'admin.*'},
]

# django-extra-checks
# https://github.com/kalekseev/django-extra-checks

EXTRA_CHECKS = {
    'checks': [
        # Forbid `unique_together`:
        'no-unique-together',
        # Require non empty `upload_to` argument:
        'field-file-upload-to',
        # Use the indexes option instead:
        'no-index-together',
        # FileField/ImageField must have non empty `upload_to` argument:
        'field-file-upload-to',
        # Text fields shoudn't use `null=True`:
        'field-text-null',
        # Prefer using BooleanField(null=True) instead of NullBooleanField:
        'field-boolean-null',
        # Don't pass `null=False` to model fields (this is django default)
        'field-null',
        # ForeignKey fields must specify db_index explicitly if used in
        # other indexes:
        {'id': 'field-foreign-key-db-index', 'when': 'indexes'},
        # If field nullable `(null=True)`,
        # then default=None argument is redundant and should be removed:
        'field-default-null',

        # verbose_name must use gettext
        'field-verbose-name-gettext',
        # help_text must use gettext
        'field-help-text-gettext',
        # require `verbose_name` and `verbose_name_plural` for all models
        {'id': 'model-meta-attribute',
         'attrs': ['verbose_name', 'verbose_name_plural'], 'level': 'CRITICAL'},
        # ModelSerializer's extra_kwargs must not include fields that specified on serializer.
        'drf-model-serializer-extra-kwargs',
        # Each ModelSerializer.Meta must have all attributes specified in attrs
        {'id': 'drf-model-serializer-meta-attribute', 'attrs': ['read_only_fields']},
    ],
}

SILKY_PYTHON_PROFILER = False

MIDDLEWARE += (
    # https://github.com/jazzband/django-silk#installation
    'silk.middleware.SilkyMiddleware',
    # https://github.com/bradmontgomery/django-querycount
    # Prints how many queries were executed, useful for the APIs.
    'querycount.middleware.QueryCountMiddleware',
)
