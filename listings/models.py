from django.db import models
from datetime import datetime
from lenders.models import Lender
# Create your models here.


class Listing(models.Model):
    programoriginator = models.TextField(max_length=400,blank=True,verbose_name="Program Originator") # ---> Program Originator
    programname = models.CharField(max_length=400,blank=True,verbose_name="Program Name")   # ---> Program Name
    programtype = models.CharField(max_length=500,blank=True,verbose_name="Program Type")    # --->  Program Type
    programdistribution = models.CharField(max_length=400,blank=True,verbose_name="Program Distribution")
    programcontact = models.CharField(max_length=400,blank=True,verbose_name="Program Contact")
    participatinglenders = models.CharField(max_length=400,blank=True,verbose_name="Participating Lender")
    link = models.CharField(max_length=500,blank=True,verbose_name="Link")
    address = models.CharField(max_length=400,blank=True)
    city = models.CharField(max_length=500,blank=True)
    state = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=2,blank=True)
    zipcode = models.CharField(max_length=300,blank=True,verbose_name="Zip Code")
    firstbuyersonly = models.CharField(max_length=100,blank=True,verbose_name="First Time Buyers Only?")
    ataglance = models.CharField(max_length=100,blank=True,verbose_name="At a glance")
    canbecombined = models.CharField(max_length=100,blank=True,verbose_name="Can be combined?")
    canbecombinedwith = models.CharField(max_length=400,blank=True,verbose_name="Can be combined with")
    requiresinspection = models.CharField(max_length=100,blank=True,verbose_name="Requires Inspection?")
    mustbeprimary = models.CharField(max_length=100,blank=True,verbose_name="Must be primay residence?")
    creditrequirment = models.CharField(max_length=100,blank=True,verbose_name="Credit Requirement")
    employerparticipation = models.CharField(max_length=100,blank=True,verbose_name="Employer Participation")
    maxdebtotincome = models.CharField(max_length=100,blank=True,verbose_name="Max Debt to Income Ratio")
    description = models.TextField(max_length=1000,blank=True,verbose_name="Description")
    Neighborhoods = models.TextField(blank=True)
    blocks = models.TextField(max_length=100,blank=True)
    amount = models.CharField(max_length=100,blank=True,null=True,verbose_name="Amount")
    ami = models.IntegerField(blank=True,null=True,verbose_name="AMI")
    minimumcontribution = models.IntegerField(null=True,verbose_name="Minimum Contribution")
    mortgageamount = models.CharField(max_length=100,blank=True,null=True,verbose_name="Mortgage Amount")
    amountofassistance = models.CharField(max_length=100,blank=True,null=True,verbose_name="Amount of Asistance")
    eligible = models.TextField(max_length=400,blank=True)
    getstarted = models.TextField(max_length=500,blank=True,verbose_name="Get Started")
    eligibilitylimitations = models.TextField(max_length=400,blank=True,verbose_name="Eligibility Limitations")
    amilimit = models.TextField(blank=True,null=True,verbose_name="AMI Limit")
    householdincomerestrictions = models.TextField(max_length=50,blank=True,verbose_name="Household Income Restrictions")
    mustearncounselingcertificate = models.TextField(max_length=50,blank=True,verbose_name="Must earn Counseling Certificate?")
    fixedratemortgagesonly = models.TextField(max_length=50,blank=True,verbose_name="Fixed Rate Mortages Only?")
    is_published=models.BooleanField(default=True,blank=True)
    # list_date = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.programname
  
    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'

class Searchsave(models.Model):
   phrase = models.CharField(max_length=100)
   link_visited = models.CharField(max_length=300,blank=True)
   misc = models.CharField(max_length=100,blank=True)
   length = models.IntegerField(blank=True)
   time_visited = models.DateTimeField(default=datetime.now,blank=True)
   user_id = models.IntegerField(blank=True)
   def __str__(self):
        return self.phrase

