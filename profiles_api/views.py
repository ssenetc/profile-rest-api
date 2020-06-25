
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializer_class= serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIViews features"""
        an_apiview=[
            'hi','how','are','you',
        ]

        return Response({'key1':'value','key2':an_apiview})


    def post(self,request):
        """Create a hello message with the input provided by user"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})

        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
                            )

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})


    def patch(self,request,pk=None):
        """Handles partial updating of an object"""
        return Response({'method':'PATCH'})


    def delete(self, request,pk=None):
        """Deletes an object"""
        return Response({'method':'DELETE'})
