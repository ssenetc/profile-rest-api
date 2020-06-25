
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

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





class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class=serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset=[
            'This is an typical example of a viewset'
        ]
        return Response({'message':'message1','a_viewset':a_viewset})

    def create(self,request):
        """Create a hello message"""
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!!!'

            return Response({'message':message})
        else:
            return Response(
            serializer.errors,status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """handle getting an objest by its ID"""
        return Response({'HTTP method':'GET'})

    def update(self,request,pk=None):
        """handles updating an object"""
        return Response({'HTTP method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handles updating an object partially"""
        return Response({'HTTP method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handles removing an object """
        return Response({'HTTP method':'DELETE'})
