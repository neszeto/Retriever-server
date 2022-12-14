from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from django.contrib.auth.models import User


class UserView(ViewSet):
    """Retriever patient view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single user"""

    def list(self, request):
        """Handle GET requests for all users"""

        if "loggedin" in request.query_params:
            doctors = User.objects.filter(pk=request.auth.user_id)
        else:
            try:
                doctors = User.objects.all()
            
            except User.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(doctors, many=True)
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""

    class Meta: 
        model = User
        fields = ('id', 'first_name', 'last_name')