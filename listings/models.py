from django.db import models
from datetime import datetime
from lenders.models import Lender
# Create your models here.

class Listing(models.Model):
    programoriginator = models.TextField(max_length=400,blank=True) # ---> Program Originator
    programname = models.CharField(max_length=400,blank=True)   # ---> Program Name
    programtype = models.CharField(max_length=500,blank=True)    # --->  Program Type
    programdistribution = models.CharField(max_length=400,blank=True)
    programcontact = models.CharField(max_length=400,blank=True)
    participatinglenders = models.CharField(max_length=400,blank=True)
    link = models.CharField(max_length=500,blank=True)
    address = models.CharField(max_length=400,blank=True)
    city = models.CharField(max_length=500,blank=True)
    state = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=2,blank=True)
    zipcode = models.CharField(max_length=300,blank=True)
    firstbuyersonly = models.CharField(max_length=100,blank=True)
    ataglance = models.CharField(max_length=100,blank=True)
    canbecombined = models.CharField(max_length=100,blank=True)
    canbecombinedwith = models.CharField(max_length=400,blank=True)
    requiresinspection = models.CharField(max_length=100,blank=True)
    mustbeprimary = models.CharField(max_length=100,blank=True)
    creditrequirment = models.CharField(max_length=100,blank=True)
    employerparticipation = models.CharField(max_length=100,blank=True)
    maxdebtotincome = models.CharField(max_length=100,blank=True)
    description = models.TextField(max_length=1000,blank=True,)
    Neighborhoods = models.TextField(blank=True)
    blocks = models.TextField(max_length=100,blank=True)
    amount = models.CharField(max_length=100,blank=True,null=True)
    ami = models.IntegerField(blank=True,null=True)
    minimumcontribution = models.IntegerField(null=True)
    mortgageamount = models.CharField(max_length=100,blank=True,null=True)
    amountofassistance = models.CharField(max_length=100,blank=True,null=True)
    eligible = models.TextField(max_length=400,blank=True)
    getstarted = models.TextField(max_length=500,blank=True)
    eligibilitylimitations = models.TextField(max_length=400,blank=True)
    amilimit = models.TextField(blank=True,null=True)
    householdincomerestrictions = models.TextField(max_length=50,blank=True)
    mustearncounselingcertificate = models.TextField(max_length=50,blank=True)
    fixedratemortgagesonly = models.TextField(max_length=50,blank=True)
    is_published=models.BooleanField(default=True,blank=True)
    # list_date = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.programname


class Searchsave(models.Model):
   phrase = models.CharField(max_length=100)
   link_visited = models.CharField(max_length=300,blank=True)
   misc = models.CharField(max_length=100,blank=True)
   length = models.IntegerField(blank=True)
   time_visited = models.DateTimeField(default=datetime.now,blank=True)
   user_id = models.IntegerField(blank=True)
   def __str__(self):
        return self.phrase