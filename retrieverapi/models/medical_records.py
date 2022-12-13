from django.db import models
from django.contrib.auth.models import User

class MedicalRecords(models.Model):
    """Database model for Medical Records"""
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='records_written_by_doctor')
    patient = models.ForeignKey('Patients', on_delete=models.CASCADE, related_name='records_for_patient')
    presenting_complaint = models.CharField(max_length=55)
    subjective = models.TextField()
    objective = models.TextField()
    assessment = models.TextField()
    plan = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    diagnosis = models.ForeignKey('Diagnoses', on_delete=models.CASCADE, related_name='records_with_diagnosis')
    medications = models.ManyToManyField('Medications', through='MedicalRecordMedications')



    @property
    def my_record(self):
        return self.__my_record

    @my_record.setter
    def my_record(self, value):
        self.__my_record = value


    