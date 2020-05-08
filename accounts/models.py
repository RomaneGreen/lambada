from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.TextField(max_length=200, blank=True)
    employer = models.CharField(max_length=200, blank=True)
    householdincome = models.CharField(max_length=200, blank=True)
    familysize = models.CharField(max_length=200, blank=True)
    veteran = models.CharField(max_length=100, blank=True)
    firsttimebuyer = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.user.username


