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

    def create(self, request):
        """Handle POST requests"""
        currentMedications = Medications.objects.all()
        
        if any(request.data["name"].lower() == medication.name.lower() for medication in currentMedications):
            return Response({"message": "This medication already exists"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if request.data['name'] == "":
            return Response({"message": "No medication was entered"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            create_medication = Medications.objects.create(
                name=request.data["name"]
            )
            serializer = MedicationSerializer(create_medication)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class MedicationSerializer(serializers.ModelSerializer):
    """JSON serializer for medications"""

    class Meta: 
        model = Medications
        fields = ('id', 'name')