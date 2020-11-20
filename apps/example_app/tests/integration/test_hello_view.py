from rest_framework import status


def test_latest(api):
    result = api.get('/api/v1/example_app/hello/')

    assert status.HTTP_200_OK == result.status_code
