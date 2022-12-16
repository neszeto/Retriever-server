from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from retrieverapi.models import Doctors


class DoctorView(ViewSet):
    """Retriever doctor view"""
    def retrieve(self, request, pk):
        """Handle GET requests for single doctor"""
        try: 
            doctor = Doctors.objects.get(pk=pk)
        except: 
            return Response({'message': 'the game you requested does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DoctorSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def update(self, request, pk):
        """handles PUT request to doctors"""
        doctor = Doctors.objects.get(pk=pk)

        if doctor.active is False:
            doctor.active = True
            doctor.save()
        else:
            doctor.image_url=request.data['imageUrl']
            doctor.bio=request.data['bio']
            doctor.active=['active']
            doctor.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
        


class DoctorSerializer(serializers.ModelSerializer):
    """JSON serializer for doctors"""
    
    
    class Meta: 
        model = Doctors
        fields = ('id', 'user', 'image_url', 'bio', 'active')
        