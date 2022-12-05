from django.db import models


class Patients(models.Model): 
    """Database model for Patients"""
    name = models.CharField(max_length=55)
    species = models.ForeignKey('Species', on_delete=models.CASCADE, related_name='patients_of_that_species')
    sex = models.CharField(max_length=10)
    breed = models.CharField(max_length=55)
    age = models.IntegerField(default=0)
    color = models.CharField(max_length=25)
    weight = models.IntegerField(default=0)
    deceased = models.BooleanField(default=False)
    owner = models.ForeignKey('Owners', on_delete=models.CASCADE, related_name='patients_of_owner')