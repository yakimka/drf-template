from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(('GET',))
def hello_view(request, **kwargs):
    return Response({'result': 'hello!'})
