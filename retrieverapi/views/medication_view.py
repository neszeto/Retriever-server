from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from retrieverapi.models import Medications


class MedicationView(ViewSet):
    """Retriever patient view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single medication"""

    def list(self, request):
        """Handle GET requests for all medications"""
        try:
            doctors = Medications.objects.all()
            serializer = MedicationSerializer(doctors, many=True)
            return Response(serializer.data)
        except Medications.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


class MedicationSerializer(serializers.ModelSerializer):
    """JSON serializer for medications"""

    class Meta: 
        model = Medications
        fields = ('id', 'name')