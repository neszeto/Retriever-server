from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retrieverapi.models import MedicalRecords, Diagnoses, MedicalRecordMedications
from django.contrib.auth.models import User


class MedicalRecordView(ViewSet):
    """Retriever medical record view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single medical record"""
        try: 
            game = MedicalRecords.objects.get(pk=pk)
        except: 
            return Response({'message': 'the medical record you requested does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MedicalRecordsSerializer(game)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests for all medical records"""
        if "patient" in request.query_params:
            
            patient_id = request.query_params['patient']
            records = MedicalRecords.objects.filter(patient=patient_id).order_by('-date')
            
         
        else:
            try:
                records = MedicalRecords.objects.all()
                
            except MedicalRecords.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        for record in records:
            if request.auth.user == record.doctor.id:
                record.my_record = True
            else:
                record.my_record = False

        
        serializer = MedicalRecordsSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle POST requests"""
        record = MedicalRecords.objects.create(
            name=request.data["name"],
            phone_number=request.data["phoneNumber"],
            email=request.data["email"],
            address=request.data["address"]

        )
        serializer = MedicalRecordsSerializer(record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class DiagnosisSerializer(serializers.ModelSerializer):
    """JSON serializer for diagnosis"""
    class Meta:
        model = Diagnoses
        fields = ('diagnosis', )

class DoctorSerializer(serializers.ModelSerializer):
    """JSON serializer for doctors"""
    class Meta: 
        model= User
        fields = ('id', 'first_name', 'last_name')

class MedicationSerializer(serializers.ModelSerializer):
    """JSON serializer for medications"""
    class Meta:
        model = MedicalRecordMedications
        fields = ('medication', )
        depth=1

class MedicalRecordsSerializer(serializers.ModelSerializer):
    """JSON serializer for medical records"""
    doctor = DoctorSerializer(many=False)
    diagnosis = DiagnosisSerializer(many=False)
    medications_on_record = MedicationSerializer(many=True)

    class Meta: 
        model = MedicalRecords
        fields = ('id', 'doctor', 'patient', 'presenting_complaint', 'subjective', 'objective', 'assessment', 'plan', 'date', 'diagnosis', 'medications_on_record', 'my_record')
        