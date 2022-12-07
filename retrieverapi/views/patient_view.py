from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retrieverapi.models import Patients, Owners, Species


class PatientView(ViewSet):
    """Retriever patient view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single patient"""

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
        


class PatientSerializer(serializers.ModelSerializer):
    """JSON serializer for patients"""

    class Meta: 
        model = Patients
        fields = ('id', 'name', 'species', 'sex', 'breed', 'age', 'color', 'weight', 'deceased', 'owner', 'image_url')
        depth=1