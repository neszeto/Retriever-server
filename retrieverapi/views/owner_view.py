from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retrieverapi.models import Owners


class OwnerView(ViewSet):
    """Retriever owner view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single owner"""

    def list(self, request):
        """Handle GET requests for all owners"""
        try:
            owner = Owners.objects.all()
            serializer = OwnersSerializer(owner, many=True)
            return Response(serializer.data)
        except Owners.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    def create(self, request):
        """Handle POST requests"""
        owner = Owners.objects.create(
            name=request.data["name"],
            phone_number=request.data["phoneNumber"],
            email=request.data["email"],
            address=request.data["address"]

        )
        serializer = OwnersSerializer(owner)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OwnersSerializer(serializers.ModelSerializer):
    """JSON serializer for patients"""

    class Meta: 
        model = Owners
        fields = ('id', 'name', 'phone_number', 'email', 'address')