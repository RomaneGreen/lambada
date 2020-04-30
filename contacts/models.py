from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
   listing = models.CharField(max_length=300)
   listing_id = models.IntegerField()
   name = models.CharField(max_length=300,blank=True)
   email = models.CharField(max_length=200,blank=True)
   phone = models.CharField(max_length=200,blank=True)
   message = models.TextField(blank=True)
   contact_date = models.DateTimeField(default=datetime.now,blank=True)
   user_id = models.IntegerField(blank=True)
   def __str__(self):
      return self.name