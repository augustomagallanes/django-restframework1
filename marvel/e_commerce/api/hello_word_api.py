from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(http_method_names=['GET'])
def hello_world_api_view(request):
    _data = {"datos": "hola_mundo"}
    return Response(data=_data, status=status.HTTP_200_OK)