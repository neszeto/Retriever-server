from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retrieverapi.models import Diagnoses


class DiagnosisView(ViewSet):
    """Retriever patient view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single diagnosis"""

    def list(self, request):
        """Handle GET requests for all diagnoses"""
        try:
            diagnosis = Diagnoses.objects.all()
            serializer = DiagnosesSerializer(diagnosis, many=True)
            return Response(serializer.data)
        except Diagnoses.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        """Handle POST requests"""
        all_diagnoses = Diagnoses.objects.all()

        if any(request.data["diagnosis"].lower() == diagnosis.diagnosis.lower() for diagnosis in all_diagnoses): #if the diagnosis exists in the database
            foundDiagnosis = next(diagnosis for diagnosis in all_diagnoses if diagnosis.diagnosis.lower() == request.data["diagnosis"].lower()) #find that diagnosis object and return it
            serializer = DiagnosesSerializer(foundDiagnosis)
            return Response(serializer.data, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        else: #if the diagnosis does not exist in the database, create it and return it
            diagnosis = Diagnoses.objects.create(
                diagnosis=request.data["diagnosis"]
            )
            serializer = DiagnosesSerializer(diagnosis)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class DiagnosesSerializer(serializers.ModelSerializer):
    """JSON serializer for diagnoses"""

    class Meta: 
        model = Diagnoses
        fields = ('id', 'diagnosis')