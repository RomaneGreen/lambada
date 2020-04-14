from django.shortcuts import render,get_object_or_404,redirect
from .models import Listing
from .models import Searchsave
from listings.choices import price_choices,bedroom_choices,state_choices
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import requests
from django.contrib import messages

# Create your views here.


def index(request):
   ipdata = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
   ipmapinfo = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
   r = requests.get('https://www.iplocate.io/api/lookup/'+ipmapinfo)
   your_lat = r.json()['latitude']
   your_lon = r.json()['longitude']
   my_lat = '40.663918'
   my_lon = '-73.8820097'
   my_ip = '24.187.82.109'
   listings = Listing.objects.order_by('-list_date').filter(is_published=True)
   mapbox_access_token = 'pk.eyJ1Ijoicm9tYW5lNzExOTMiLCJhIjoiY2s4cTQ1eGRyMDBjdDNtb2RzcjRiZWluNyJ9._Ju--uLYkgFY7wPsxp5PbA'

   paginator = Paginator(listings, 1)
   page = request.GET.get('page')
   paged_listings = paginator.get_page(page)

   context = {
       'listings': paged_listings,
       'mapbox_access_token': mapbox_access_token,
       'my_lat': my_lat,
       'my_lon': my_lon
   }

 
   print('wow',your_lat,your_lon,r.json())
   return render(request,'listings/listings.html',context)



def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
      'listing': listing,
    
  }
  return render(request,'listings/listing.html',context)



def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    
    if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+keywords+'&key=AIzaSyBbqO1MJZ55ohsVhEGj-v8-RAUJj-HwGuc')
      print("dannnnmm",r.json())
      if keywords:
        queryset_list = queryset_list.filter(description__icontains=keywords)
        
    if 'city' in request.GET:
        keywords = request.GET['city']
        print('kword',keywords)
        search_term = keywords
        user_id = request.GET['user_id'] 
        print(user_id,"uuidxxxx")
        link = request.get_full_path()
        print('request',link,)
        if request.user.is_authenticated:
          user_id = request.user.id
          has_visited = Searchsave.objects.all().filter(phrase=search_term,user_id=user_id)
          if has_visited:
              wishlist = Searchsave.objects.filter(phrase=search_term,user_id=user_id)
              wishlist.delete()
        if keywords:
            queryset_list = queryset_list.filter(Q(city__icontains=keywords) |
             Q(state__icontains=keywords) |  Q(zipcode__iexact=keywords) | 
              Q(Neighborhoods__icontains=keywords)  |  Q(country__icontains=keywords)  |  Q(address__icontains=keywords)  )
        length = queryset_list.count()

        searchsaved = Searchsave(phrase=search_term,link_visited=link,length=queryset_list.count(),user_id=user_id)
        searchsaved.save()
      
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
    r = "hi server"
    # r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+keywords+'&key=AIzaSyBbqO1MJZ55ohsVhEGj-v8-RAUJj-HwGuc')
    # print("dannnnmm",r.json()['results'])
    return render(request,'listings/search.html',context)