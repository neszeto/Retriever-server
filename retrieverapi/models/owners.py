from django.db import models

class Owners(models.Model):
    """Database model for Owners"""
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=100)