from django.db import models

class Diagnoses(models.Model):
    """Database model for Diagnoses"""
    diagnosis = models.CharField(max_length=100)