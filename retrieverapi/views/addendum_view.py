from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retrieverapi.models import Addendums, MedicalRecords
from datetime import date


class AddendumView(ViewSet):
    """Retriever addendum view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single addendum"""

    def list(self, request):
        """Handle GET requests for all addendums"""
        try:
            addendums = Addendums.objects.all()
            serializer = AddendumSerializer(addendums, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Addendums.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        """Handle POST addendums"""
        medical_record = MedicalRecords.objects.get(pk=request.data["medicalRecordId"])
        addendum = Addendums.objects.create(
            medical_record=medical_record,
            addendum = request.data["addendum"],
            created_on = date.today()
        )
        serializer = AddendumSerializer(addendum)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """handle DELETE requests for games"""
        addendum = Addendums.objects.get(pk=pk)
        addendum.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class AddendumSerializer(serializers.ModelSerializer):
    """JSON serializer for addendums"""

    class Meta: 
        model = Addendums
        fields = ('id', 'medical_record', 'addendum', 'created_on')