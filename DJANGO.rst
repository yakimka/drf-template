Django
======


Configuration
-------------

We share the same configuration structure for almost every possible
environment.

We use:

- ``django-split-settings`` to organize ``django``
  settings into multiple files and directories
- ``.env`` files to store secret configuration
- ``python-decouple`` to load ``.env`` files into ``django``

Components
~~~~~~~~~~

If you have some specific components like ``celery`` or ``mailgun`` installed,
they could be configured in separate files.
Just create a new file in ``server/settings/components/``.
Then add it into ``server/settings/__init__.py``.

Environments
~~~~~~~~~~~~

To run ``django`` on different environments just
specify ``DJANGO_ENV`` environment variable.
It must have the same name as one of the files
from ``server/settings/environments/``.
Then, values from this file will override other settings.

Local settings
~~~~~~~~~~~~~~

If you need some specific local configuration tweaks,
you can create file ``server/settings/environments/local.py.template``
to ``server/settings/environments/local.py``.
It will be loaded into your settings automatically if exists.

.. code:: bash

  cp server/settings/environments/local.py.template server/settings/environments/local.py

See ``local.py.template`` version for the reference.


Secret settings
---------------

We use ``.env`` files for ``django``, ``postgres``, ``docker``, etc.

Initially, you will need to copy file
``config/.env.template`` to ``config/.env``:

.. code:: bash

  cp config/.env.template config/.env

When adding any new secret ``django`` settings you will need to:

1. Add new key and value to ``config/.env``
2. Add new key without value to ``config/.env.template``,
   add a comment on how to get this value for other users
3. Add new variable inside ``django`` settings
4. Use ``python-decouple`` to load this ``env`` variable like so:
   ``MY_SECRET = config('MY_SECRET')``


Extensions
----------

We use different ``django`` extensions that make your life easier.
Here's a full list of the extensions for both development and production:

- `django-split-settings`_ - organize
  ``django`` settings into multiple files and directories.
  Easily override and modify settings.
  Use wildcards in settings file paths and mark settings files as optional
- `django-cors-headers`_ - django app for handling the server headers required
  for Cross-Origin Resource Sharing (CORS)
- `django-extensions`_ -  is a collection of custom extensions
  for the Django Framework.
- `django-prometheus`_ - export Django monitoring metrics for Prometheus.io
- `django-rest-framework`_ - is a powerful and flexible toolkit for
  building Web APIs
- `sentry-sdk`_ - Python SDK for Sentry.io

Development only extensions:

- `django-silk`_ - a configurable set of panels that
  display various debug information about the current request/response
- `django-querycount`_ - middleware that prints the number
  of DB queries to the runserver console
- `nplusone`_ - auto-detecting the `n+1 queries problem`_ in ``django``
- `django-extra-checks`_ - auto-detecting the `n+1 queries problem`_ in ``django``

.. _django-split-settings: https://github.com/sobolevn/django-split-settings
.. _django-cors-headers: https://github.com/adamchainz/django-cors-headers
.. _django-extensions: https://github.com/django-extensions/django-extensions
.. _django-prometheus: https://github.com/korfuri/django-prometheus
.. _django-rest-framework: https://github.com/encode/django-rest-framework
.. _sentry-sdk: https://github.com/getsentry/sentry-python
.. _django-silk: https://github.com/jazzband/django-silk
.. _django-querycount: https://github.com/bradmontgomery/django-querycount
.. _nplusone: https://github.com/jmcarp/nplusone
.. _`n+1 queries problem`: https://stackoverflow.com/questions/97197/what-is-the-n1-select-query-issue
.. _django-extra-checks: https://github.com/kalekseev/django-extra-checks


Further reading
---------------

- `django-split-settings tutorial <https://medium.com/wemake-services/managing-djangos-settings-e2b7f496120d>`_
- `docker env-file docs <https://docs.docker.com/compose/env-file/>`_


Django admin
~~~~~~~~~~~~

- `Django Admin Cookbook <https://books.agiliq.com/projects/django-admin-cookbook/en/latest/>`_
