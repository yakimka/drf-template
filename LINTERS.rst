Linters
=======

This project uses several linters to make coding style consistent.
All configuration is stored inside ``setup.cfg``.


Plugins
-------

Things that are included in the linting process:

- `flake8 <http://flake8.pycqa.org/>`_ is used a general tool for linting
- `bandit <https://github.com/PyCQA/bandit>`_ for static security checks
- and more!

Running linting process for all ``python`` files in the project:

.. code:: bash

  make lint

Extra plugins
~~~~~~~~~~~~~

We also use some extra plugins for ``flake8``
that are not bundled with ``wemake-python-styleguide``:

- `flake8-pytest <https://github.com/vikingco/flake8-pytest>`_ - ensures that ``pytest`` best practices are used
- `flake8-pytest-style <https://github.com/m-burst/flake8-pytest-style>`_ - ensures that ``pytest`` tests and fixtures are written in a single style
- `flake8-django <https://github.com/rocioar/flake8-django>`_ - plugin to enforce best practices in a ``django`` project
