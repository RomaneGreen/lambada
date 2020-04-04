from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from lenders.models import Lender

def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'listings': listings
    }       
    return render(request,'pages/index.html',context)


def about(request):
    lenders = Lender.objects.order_by('-programdate')

    #get lender 
    mvp_lenders = Lender.objects.all().filter(is_mvp=True)

    context = {
        'lenders': lenders,
        'mvp_lenders': mvp_lenders
    } 
    return render(request,'pages/about.html',context)


