from django.db import models


class Species(models.Model):
    """Database model for Species"""
    species = models.CharField(max_length=50)