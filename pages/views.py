from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.choices import price_choices,bedroom_choices,state_choices
from lenders.models import Lender

def index(request):

    listings = Listing.objects.order_by('id').filter(is_published=True)[:6]
    context = {
        'listings': listings,    
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
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


