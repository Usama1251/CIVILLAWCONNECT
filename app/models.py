from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    # Add more fields as needed

    def __str__(self):
        return self.user.username
