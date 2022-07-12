from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from user_app.models import UserTable
from .serializers import UserSerializer


@api_view(['GET'])
def getData(request):
    person = {'name': 'Dennis', 'age': 28}
    return Response(person)


@api_view(['POST'])
def postData(request):
    print(request.data)
    return Response()


@api_view(['POST'])
def api_login_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
