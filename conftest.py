import pytest
from model_bakery import baker as baker_
from rest_framework.test import APIClient

from main_app.test.factory import Factory


@pytest.fixture()
def factory(db):
    return Factory


@pytest.fixture()
def baker(db):
    return baker_


@pytest.fixture()
def api():
    return APIClient()
