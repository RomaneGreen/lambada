from django.db import models
from datetime import datetime
from lenders.models import Lender
# Create your models here.

class Listing(models.Model):
    lender = models.ForeignKey(Lender,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    link = models.CharField(max_length=300)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=2,blank=True)
    zipcode = models.CharField(max_length=20)
    firstbuyersonly = models.CharField(max_length=100)
    ataglance = models.CharField(max_length=100)
    canbecombined = models.CharField(max_length=100)
    requiresinspection = models.CharField(max_length=100)
    mustbeprimary = models.CharField(max_length=100)
    creditrequirment = models.CharField(max_length=100)
    employerparticipation = models.CharField(max_length=100)
    maxdebtotincome = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    Neighborhoods = models.TextField(blank=True)
    amount = models.IntegerField(blank=True)
    minimumcontribution = models.IntegerField(blank=True)
    mortgageamount = models.IntegerField(blank=True)
    amountofassistance = models.IntegerField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published=models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title


class Searchsave(models.Model):
   phrase = models.CharField(max_length=100)
   link_visited = models.CharField(max_length=300,blank=True)
   misc = models.CharField(max_length=100,blank=True)
   length = models.IntegerField(blank=True)
   time_visited = models.DateTimeField(default=datetime.now,blank=True)
   user_id = models.IntegerField(blank=True)
   def __str__(self):
        return self.phrase