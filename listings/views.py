from django.shortcuts import render,get_object_or_404
from .models import Listing
from listings.choices import price_choices,bedroom_choices,state_choices
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def index(request):
   listings = Listing.objects.order_by('-list_date').filter(is_published=True)

   paginator = Paginator(listings, 1)
   page = request.GET.get('page')
   paged_listings = paginator.get_page(page)

   context = {
       'listings': paged_listings
   }

 

   return render(request,'listings/listings.html',context)



def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
      'listing': listing
  }
  return render(request,'listings/listing.html',context)



def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      if keywords:
        queryset_list = queryset_list.filter(description__icontains=keywords)
      
    if 'city' in request.GET:
        keywords = request.GET['city']
        if keywords:
            queryset_list = queryset_list.filter(Q(city__icontains=keywords) | Q(state__icontains=keywords) |  Q(zipcode__iexact=keywords) |  Q(Neighborhoods__icontains=keywords) ) 
    
    if 'state' in request.GET:
        keywords = request.GET['state']
        if keywords:
            queryset_list = queryset_list.filter(state__iexact=keywords)  
    
    if 'bedrooms' in request.GET:
        keywords = request.GET['bedrooms']
        if keywords:
            queryset_list = queryset_list.filter(id__lte=keywords)   

    if 'price' in request.GET:
        keywords = request.GET['price']
        if keywords:
            queryset_list = queryset_list.filter(minimumcontribution__lte=keywords)  



    context = {
      
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
        # 'listings': queryset_listing
    }  
    return render(request,'listings/search.html',context)