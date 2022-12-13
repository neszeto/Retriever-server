from django.db import models

class Addendums(models.Model):
    """Database model for Diagnoses"""
    medical_record = models.ForeignKey('MedicalRecords', on_delete=models.CASCADE, related_name='record_addendums')
    addendum = models.TextField()
    created_on = models.DateField(auto_now=True)