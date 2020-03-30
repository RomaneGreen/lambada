from django.db import models
from datetime import datetime

# Create your models here.
class Lender(models.Model):
    name = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    phone = models.CharField(max_length=20,blank=True)
    programdate = models.DateTimeField(default=datetime.now,blank=True)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=300,blank=True)
    location = models.TextField(max_length=300)
    email = models.CharField(max_length=300)
    is_mvp = models.BooleanField(default=False)
    def __str__(self):
        return self.name

        