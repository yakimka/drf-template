# Caching
# https://docs.djangoproject.com/en/3.1/topics/cache/

CACHES = {
    'default': {
        # TODO: use some other cache in production,
        # like https://github.com/jazzband/django-redis
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
