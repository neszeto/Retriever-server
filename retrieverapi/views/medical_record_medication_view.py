from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retrieverapi.models import MedicalRecordMedications, MedicalRecords, Medications


class MedicalRecordMedicationView(ViewSet):
    """Retriever medical record medications view"""
    def retrieve(self, request, pk):
        """Handle GET requests for MRM"""

    def list(self, request):
        """Handle GET requests for all MRMs"""
        all = MedicalRecordMedications.objects.all()

        serializer = MedicalRecordMedicationsSerializer(all, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle POST requests"""
        medical_record = MedicalRecords.objects.get(pk=request.data["medicalRecordId"])
        medication = Medications.objects.get(pk=request.data["medicationId"])

        medical_record_medication = MedicalRecordMedications.objects.create(
            medical_record= medical_record,
            medication=medication
        )
        serializer = MedicalRecordMedicationsSerializer(medical_record_medication)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MedicalRecordMedicationsSerializer(serializers.ModelSerializer):
    """JSON serializer for MRM"""

    class Meta: 
        model = MedicalRecordMedications
        fields = ('id', 'medical_record', 'medication')
        