
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIViews features"""
        an_apiview=[
            'hi','how','are','you',
        ]

        return Response({'key1':'value','key2':an_apiview})
