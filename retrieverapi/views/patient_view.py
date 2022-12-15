from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retrieverapi.models import Patients, Owners, Species, MedicalRecords


class PatientView(ViewSet):
    """Retriever patient view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single patient"""
        try: 
            game = Patients.objects.get(pk=pk)
        except: 
            return Response({'message': 'the game you requested does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PatientSerializer(game)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests for all patients"""
        try:
            patients = Patients.objects.order_by('name')
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data)
        except Patients.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """Handles POST operations"""
        owner = Owners.objects.get(pk=request.data["ownerId"])
        species = Species.objects.get(pk=request.data["speciesId"])

        if request.data["image"] is "":
            patient = Patients.objects.create(
                name=request.data["name"],
                species=species,
                sex=request.data["sex"],
                breed=request.data["breed"],
                age=request.data["age"],
                color=request.data["color"],
                weight=request.data["weight"],
                owner=owner,
                image_url="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__480.png"
            )
        else:
            patient = Patients.objects.create(
                name=request.data["name"],
                species=species,
                sex=request.data["sex"],
                breed=request.data["breed"],
                age=request.data["age"],
                color=request.data["color"],
                weight=request.data["weight"],
                owner=owner,
                image_url=request.data["image"]
            )

        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """handles PUT request to patients"""
        species = Species.objects.get(pk=request.data["speciesId"])

        patient = Patients.objects.get(pk=pk)
        patient.name = request.data["name"]
        patient.breed = request.data["breed"]
        patient.age = request.data["age"]
        patient.color = request.data["color"]
        patient.weight = request.data["weight"]
        patient.sex = request.data["sex"]
        patient.image_url = request.data["image_url"]
        patient.deceased = request.data["deceased"]
        patient.species = species
        patient.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalRecords
        fields = ('diagnosis', 'medications')
        depth=1

class PatientSerializer(serializers.ModelSerializer):
    """JSON serializer for patients"""
    records_for_patient = RecordSerializer(many=True)
    
    class Meta: 
        model = Patients
        fields = ('id', 'name', 'species', 'sex', 'breed', 'age', 'color', 'weight', 'deceased', 'owner', 'image_url', 'records_for_patient')
        depth=1