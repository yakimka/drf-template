Testing
=======

We run tests with `pytest <https://pytest.org/>`_ framework.


pytest
------

``pytest`` is the main tool for test discovery, collection, and execution.
It is configured inside ``setup.cfg`` file.

We use a lot of ``pytest`` plugins that enhance our development experience.
List of these plugins is available inside ``pyproject.toml`` file.

Running:

.. code:: bash

  make test

We also have some options that are set on each run via ``--addopts``
inside the ``setup.cfg`` file.

Plugins
~~~~~~~

We use different ``pytest`` plugins to make our testing process better.
Here's the full list of things we use:

- `pytest-django`_ - plugin that introduce a lot of ``django`` specific
  helpers, fixtures, and configuration
- `pytest-cov`_ - plugin to measure test coverage
- `pytest-randomly`_ - plugin to execute tests in random order and
  also set predictable random seed, so you can easily debug
  what went wrong for tests that rely on random behavior
- `pytest-deadfixtures`_ - plugin to find unused or duplicate fixtures
- `pytest-timeout`_ - plugin to raise errors for tests
  that take too long to finish, this way you can control test execution speed
- `pytest-testmon`_ - plugin for `Test Driven Development`_ which executes
  tests that are affected by your code changes

.. _pytest-django: https://github.com/pytest-dev/pytest-django
.. _pytest-cov: https://github.com/pytest-dev/pytest-cov
.. _pytest-randomly: https://github.com/pytest-dev/pytest-randomly
.. _pytest-deadfixtures: https://github.com/jllorencetti/pytest-deadfixtures
.. _pytest-timeout: https://pypi.org/project/pytest-timeout
.. _pytest-testmon: https://github.com/tarpas/pytest-testmon
.. _`Test Driven Development`: https://en.wikipedia.org/wiki/Test-driven_development

Tweaking tests performance
~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several options you can provide or remove to make your tests faster:

- If there are a lot of tests with database access
  it may be wise to add
  `--reuse-db option <https://pytest-django.readthedocs.io/en/latest/database.html#example-work-flow-with-reuse-db-and-create-db>`_,
  so ``django`` won't recreate database on each test
- If there are a lot of migrations to perform you may also add
  `--nomigrations option <https://pytest-django.readthedocs.io/en/latest/database.html#nomigrations-disable-django-1-7-migrations>`_,
  so ``django`` won't run all the migrations
  and instead will inspect and create models directly
- Removing ``coverage``. Sometimes that an option.
  When running tests in TDD style why would you need such a feature?
  So, coverage will be calculated when you will ask for it.
  That's a huge speed up
- Removing linters. Sometimes you may want to split linting and testing phases.
  This might be useful when you have a lot of tests, and you want to run
  linters before, so it won't fail your complex testing pyramid with a simple
  whitespace violation
