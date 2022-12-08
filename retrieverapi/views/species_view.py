from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retrieverapi.models import Species


class SpeciesView(ViewSet):
    """Retriever patient view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single species"""

    def list(self, request):
        """Handle GET requests for all species"""
        try:
            species = Species.objects.all()
            serializer = SpeciesSerializer(species, many=True)
            return Response(serializer.data)
        except Species.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


class SpeciesSerializer(serializers.ModelSerializer):
    """JSON serializer for species"""

    class Meta: 
        model = Species
        fields = ('id', 'species')
        