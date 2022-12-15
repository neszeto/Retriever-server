from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retrieverapi.models import MedicalRecords, Diagnoses, MedicalRecordMedications, Patients, Addendums
from django.contrib.auth.models import User
from django.db.models import Count




class MedicalRecordView(ViewSet):
    """Retriever medical record view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single medical record"""
        try: 
            record = MedicalRecords.objects.get(pk=pk)
        except: 
            return Response({'message': 'the medical record you requested does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MedicalRecordsSerializer(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests for all medical records"""
        if "patient" in request.query_params:
            
            patient_id = request.query_params['patient']
            records = MedicalRecords.objects.filter(patient=patient_id).order_by('-date').annotate(addendum_count=Count('record_addendums'))
            
            
         
        else:
            try:
                records = MedicalRecords.objects.all()
                
            except MedicalRecords.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
        for record in records:
            if request.auth.user_id is record.doctor_id:
                record.my_record = True
            else:
                record.my_record = False

        
        serializer = MedicalRecordsSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle POST requests"""
        if "patient" in request.query_params:
            patient_id = request.query_params['patient']

        patient=Patients.objects.get(pk=patient_id)
        doctor=User.objects.get(pk=request.data["doctorId"])
        diagnosis=Diagnoses.objects.get(pk=request.data["diagnosisId"])

        record = MedicalRecords.objects.create(
            doctor=doctor,
            patient=patient,
            presenting_complaint=request.data['presentingComplaint'],
            subjective=request.data['subjective'],
            objective=request.data['objective'],
            assessment=request.data['assessment'],
            plan=request.data['plan'],
            date=request.data['date'],
            diagnosis=diagnosis
            

        )
        serializer = MedicalRecordsSerializer(record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """handle DELETE requests"""
        record = MedicalRecords.objects.get(pk=pk)
        record.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class AddendumSerializer(serializers.ModelSerializer):
    """JSON serializer for diagnosis"""
    class Meta:
        model = Addendums
        fields = ('id', 'medical_record', 'addendum', 'created_on')

class DiagnosisSerializer(serializers.ModelSerializer):
    """JSON serializer for diagnosis"""
    class Meta:
        model = Diagnoses
        fields = ('id', 'diagnosis', )

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
    record_addendums = AddendumSerializer(many=True)
    addendum_count = serializers.IntegerField(default=None)

    class Meta: 
        model = MedicalRecords
        fields = ('id', 'doctor', 'patient', 'presenting_complaint', 'subjective', 'objective', 'assessment', 'plan', 'date', 'diagnosis', 'medications_on_record', 'my_record', 'record_addendums', 'addendum_count')




        