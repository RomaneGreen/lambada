from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.TextField(max_length=200, blank=True,verbose_name="Occupation")
    employer = models.CharField(max_length=200, blank=True,verbose_name="Employer")
    householdincome = models.CharField(max_length=200, blank=True,verbose_name="Annual Income")
    familysize = models.CharField(max_length=200, blank=True,verbose_name="Family Size")
    veteran = models.CharField(max_length=100, blank=True,verbose_name="Veteran?")
    firsttimebuyer = models.CharField(max_length=100, blank=True,verbose_name="First Time Home Buyer?")
    def __str__(self):
        return self.user.username


