from django.db import models


class MedicalRecordMedications(models.Model):
    """Database model for Medical Record Medications"""

    medical_record = models.ForeignKey('MedicalRecords', on_delete=models.CASCADE, related_name='medications_on_record')
    medication = models.ForeignKey('Medications', on_delete=models.CASCADE, related_name='records_with_medication')