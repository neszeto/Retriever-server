from django.db import models


class Medications(models.Model):
    """Database model for Medications"""
    name = models.CharField(max_length=25)
