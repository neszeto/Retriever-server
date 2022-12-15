from django.db import models
from django.contrib.auth.models import User

class Doctors(models.Model):
    """Database model for Doctors"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_that_are_doctors')
    image_url = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField()
    active = models.BooleanField(default=True)