from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
# from django.core.cache import cache
import pickle
from .models import Listing
from .models import Searchsave
from listings.choices import price_choices,bedroom_choices,state_choices
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import requests
from django.contrib import messages
import reverse_geocoder as rg
# Create your views here.


def index(request):
   ipdata = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
   ipmapinfo = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
   my_ip = '134.192.135.254' 
   my_ip = '24.187.82.109' 
   #replace my_ip with ipmapinfo in production
   r = requests.get('https://www.iplocate.io/api/lookup/'+my_ip) 
   r2 = requests.get('https://ipinfo.io/'+my_ip+'?token=bcd68a7fad37ec')
   r3 = requests.get('https://api.ipdata.co/'+my_ip+'?api-key=e4516990308595b51a3aa80f5d8f73d68d63ecd5d759d2a9702ac586')
   your_lat = r.json()['latitude']
   your_lon = r.json()['longitude']

   your_state = r2.json()['region']
   your_regcode = r3.json()['region_code']
   your_city = r.json()['city']
   your_bigcity = r2.json()['city']
   your_postal = r.json()['postal_code']

   print('NEWDATA',your_city,your_postal,your_state,your_bigcity,your_regcode)
   my_lat = '40.663918'
   my_lon = '-73.8820097'
   mapbox_access_token = 'pk.eyJ1Ijoicm9tYW5lNzExOTMiLCJhIjoiY2s4cTQ1eGRyMDBjdDNtb2RzcjRiZWluNyJ9._Ju--uLYkgFY7wPsxp5PbA'


   listings = Listing.objects.order_by('id').filter( Q(state__iexact=your_regcode)  |Q(state__iexact=your_state) | Q(state__iexact=your_bigcity)   | Q(city__iexact=your_bigcity) | Q(zipcode__iexact=your_postal) 
    | Q(Neighborhoods__icontains=your_bigcity) | Q(Neighborhoods__icontains=your_regcode)).exclude( Q(zipcode__iexact='') | Q(state__iexact='') | Q(city__iexact='')  )
      
   amount_of_results = listings.count()

   paginator = Paginator(listings, 6)
   page = request.GET.get('page')
   paged_listings = paginator.get_page(page)

   context = {
       'listings': paged_listings,
       'mapbox_access_token': mapbox_access_token,
       'my_lat': my_lat,
       'my_lon': my_lon,
       'count': amount_of_results
   }

 
   #print('wow',your_lat,your_lon,r.json())
   return render(request,'listings/listings.html',context)



def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
      'listing': listing,
    
  }
  return render(request,'listings/listing.html',context)



def search(request):
    
    queryset_list = Listing.objects.order_by('id')
    dp_list = Listing.objects.filter(programtype="Down Payment").order_by('id')
    cc_list = Listing.objects.filter(programtype="Closing Cost").order_by('id')
    fs_list = Listing.objects.filter(programtype="Forgivable Second").order_by('id')
    others_list = Listing.objects.filter(programtype="Other").order_by('id')
    # queryset_list = Listing.objects.order_by('id')
    queryset_list = Listing.objects.order_by('id')
    mapbox_access_token = 'pk.eyJ1Ijoicm9tYW5lNzExOTMiLCJhIjoiY2s4cTQ1eGRyMDBjdDNtb2RzcjRiZWluNyJ9._Ju--uLYkgFY7wPsxp5PbA'
    
    # my_lat = '40.663918'
    # my_lon = '-73.8820097'
    if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+keywords+'&key=AIzaSyBbqO1MJZ55ohsVhEGj-v8-RAUJj-HwGuc')
     # print("dannnnmm",r.json())
      if keywords:
        queryset_list = queryset_list.filter(description__icontains=keywords)
        
    if 'city' in request.GET:
        keywords = request.GET['city']
        #print('kword',keywords)
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+keywords+'&key=AIzaSyCuYOJlcMVw9bYfEw-QNgio7RQVK766-tk')
        #print("ONE",r.json()['results'][0]["geometry"]["location"]["lat"],"TWO:",r.json()['results'][0]["geometry"]["location"]["lng"])
        lat = r.json()['results'][0]["geometry"]["location"]["lat"]
        lon = r.json()['results'][0]["geometry"]["location"]["lng"]
        lat = str(lat)
        lon = str(lon)
        request.session['lat'] = lat
        request.session['lon'] = lon
        request.session['city'] = keywords
        coordinates = (lat,lon)
        results = rg.search(coordinates)
        print(results[0]['admin1'])
        print(results[0]['admin2'])
        state = results[0]['admin1']
        request.session['spate'] = state
        county = results[0]['admin2']
        print(county,state,keywords)
        # state = r2.json()['results'][0]['address_components'][3]['long_name']
        # state_abbrev = r2.json()['results'][0]['address_components'][3]['short_name']
        # county = r2.json()['results'][0]['address_components'][2]['long_name']
        # zip = r2.json()['results'][0]['address_components'][5]['long_name']
        #print(r2.json())
        search_term = keywords
        user_id = request.GET['user_id'] 
        #print(user_id,"uuidxxxx")
        link = request.get_full_path()
        request.session['link'] = link
        # page = request.GET.get('page')
        # paged_listings = paginator.get_page(page)

        print('request',link,)
        if request.user.is_authenticated:
          user_id = request.user.id
          has_visited = Searchsave.objects.all().filter(phrase=search_term,user_id=user_id)
          if has_visited:
              wishlist = Searchsave.objects.filter(phrase=search_term,user_id=user_id)
              wishlist.delete()
        if keywords:
             
             queryset_list = queryset_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
             | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state ))

             dp_list = dp_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
             | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Down Payment").order_by('id')

             cc_list = cc_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
             | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Closing Cost").order_by('id')

             fs_list = fs_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
             | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Forgivable Second").order_by('id')

             others_list = others_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
             | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Others").order_by('id')

           
        length = queryset_list.count()
    if request.method == "POST" and "savesearch" in request.POST:
        link = request.get_full_path()
        searchsaved = Searchsave(phrase=request.session['city'],link_visited=request.get_full_path(),length=queryset_list.count(),user_id=request.user.id)
        has_visited = Searchsave.objects.all().filter(phrase=request.session['city'],user_id=request.user.id)
        if has_visited:
              wishlist = Searchsave.objects.filter(phrase=request.session['city'],user_id=request.user.id)
              wishlist.delete()
        searchsaved.save()
        return redirect(request.session['link'])
    if 'state' in request.GET:
        keywords = request.GET['state']
        if keywords:
            queryset_list = queryset_list.filter(state__iexact=keywords)  
    
    if request.method == "POST" and "oopz" in request.POST:
        print("it issss",request.session['city'])
        keywords = request.session['city']     
        stt = request.session['city']
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+keywords+'&key=AIzaSyCuYOJlcMVw9bYfEw-QNgio7RQVK766-tk')
        lat = r.json()['results'][0]["geometry"]["location"]["lat"]
        lon = r.json()['results'][0]["geometry"]["location"]["lng"]
        lat = str(lat)
        lon = str(lon)
        coordinates = (lat,lon)
        results = rg.search(coordinates)
        state = results[0]['admin1']
        queryset_list = queryset_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state))

        dp_list = dp_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
             | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Down Payment").order_by('id')

        cc_list = cc_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Closing Cost").order_by('id')

        fs_list = fs_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Forgivable Second").order_by('id')

        others_list = others_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Others").order_by('id')

        
        ts = queryset_list.order_by('programname')
        amount_of_results = queryset_list.count()  
        paginator = Paginator(ts, 9)   
        page = request.GET.get('page')
        paged_listings = paginator.get_page(page)
        print("lonzg",request.session['lon'])
        print(request.session['link'])
        url = request.session['link']

        context = {
        
            'dplist': dp_list,
            'cclist': cc_list,
            'fslist': fs_list,
            'oplist': others_list,
            'bedroom_choices': bedroom_choices,
            'mapbox_access_token': mapbox_access_token,
            'price_choices': price_choices,
            'listings': paged_listings,
            'my_lon': request.session['lon'],
            'my_lat': request.session['lat'],
            'count': amount_of_results,
            'values': request.session['city'],
            # 'listings': queryset_listing
        }  
        uid = request.user.id or 0
        return render(request,'listings/search.html',context)

    if request.method == "POST" and "ztoa" in request.POST:
        print("it issss",request.session['city'])
        keywords = request.session['city']     
        stt = request.session['city']
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+keywords+'&key=AIzaSyCuYOJlcMVw9bYfEw-QNgio7RQVK766-tk')
        lat = r.json()['results'][0]["geometry"]["location"]["lat"]
        lon = r.json()['results'][0]["geometry"]["location"]["lng"]
        lat = str(lat)
        lon = str(lon)
        coordinates = (lat,lon)
        results = rg.search(coordinates)
        state = results[0]['admin1']
        queryset_list = queryset_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state))

        dp_list = dp_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
             | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Down Payment").order_by('id')

        cc_list = cc_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Closing Cost").order_by('id')

        fs_list = fs_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Forgivable Second").order_by('id')

        others_list = others_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Others").order_by('id')

        
        ts = queryset_list.order_by('-programname')
        amount_of_results = queryset_list.count()  
        paginator = Paginator(ts, 9)   
        page = request.GET.get('page')
        paged_listings = paginator.get_page(page)
        print("lonzg",request.session['lon'])
        print(request.session['link'])
        url = request.session['link']

        context = {
        
            'dplist': dp_list,
            'cclist': cc_list,
            'fslist': fs_list,
            'oplist': others_list,
            'bedroom_choices': bedroom_choices,
            'mapbox_access_token': mapbox_access_token,
            'price_choices': price_choices,
            'listings': paged_listings,
            'my_lon': request.session['lon'],
            'my_lat': request.session['lat'],
            'count': amount_of_results,
            'values': request.session['city'],
            # 'listings': queryset_listing
        }  
        uid = request.user.id or 0
        return render(request,'listings/search.html',context)

    if request.method == "POST" and "lowtohigh" in request.POST:
        print("it issss",request.session['city'])
        keywords = request.session['city']     
        stt = request.session['city']
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+keywords+'&key=AIzaSyCuYOJlcMVw9bYfEw-QNgio7RQVK766-tk')
        lat = r.json()['results'][0]["geometry"]["location"]["lat"]
        lon = r.json()['results'][0]["geometry"]["location"]["lng"]
        lat = str(lat)
        lon = str(lon)
        coordinates = (lat,lon)
        results = rg.search(coordinates)
        state = results[0]['admin1']
        queryset_list = queryset_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state))


        dp_list = dp_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
             | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Down Payment").order_by('id')

        cc_list = cc_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Closing Cost").order_by('id')

        fs_list = fs_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Forgivable Second").order_by('id')

        others_list = others_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Others").order_by('id')

        
        ts = queryset_list.order_by('amountofassistance')
        amount_of_results = queryset_list.count()  
        paginator = Paginator(ts, 9)   
        page = request.GET.get('page')
        paged_listings = paginator.get_page(page)
        print("lonzg",request.session['lon'])
        print(request.session['link'])
        url = request.session['link']

        context = {
        
            'dplist': dp_list,
            'cclist': cc_list,
            'fslist': fs_list,
            'oplist': others_list,
            'bedroom_choices': bedroom_choices,
            'mapbox_access_token': mapbox_access_token,
            'price_choices': price_choices,
            'listings': paged_listings,
            'my_lon': request.session['lon'],
            'my_lat': request.session['lat'],
            'count': amount_of_results,
            'values': request.session['city'],
            # 'listings': queryset_listing
        }  
        uid = request.user.id or 0
        return render(request,'listings/search.html',context)

    if request.method == "POST" and "typeofprogram" in request.POST:
        print("it issss",request.session['city'])
        keywords = request.session['city']     
        stt = request.session['city']
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+keywords+'&key=AIzaSyCuYOJlcMVw9bYfEw-QNgio7RQVK766-tk')
        lat = r.json()['results'][0]["geometry"]["location"]["lat"]
        lon = r.json()['results'][0]["geometry"]["location"]["lng"]
        lat = str(lat)
        lon = str(lon)
        coordinates = (lat,lon)
        results = rg.search(coordinates)
        state = results[0]['admin1']
        queryset_list = queryset_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state))


        dp_list = dp_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
             | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Down Payment").order_by('id')

        cc_list = cc_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Closing Cost").order_by('id')

        fs_list = fs_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Forgivable Second").order_by('id')

        others_list = others_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Others").order_by('id')

        
        ts = queryset_list.order_by('programtype')
        amount_of_results = queryset_list.count()  
        paginator = Paginator(ts, 9)   
        page = request.GET.get('page')
        paged_listings = paginator.get_page(page)
        print("lonzg",request.session['lon'])
        print(request.session['link'])
        url = request.session['link']

        context = {
        
            'dplist': dp_list,
            'cclist': cc_list,
            'fslist': fs_list,
            'oplist': others_list,
            'bedroom_choices': bedroom_choices,
            'mapbox_access_token': mapbox_access_token,
            'price_choices': price_choices,
            'listings': paged_listings,
            'my_lon': request.session['lon'],
            'my_lat': request.session['lat'],
            'count': amount_of_results,
            'values': request.session['city'],
            # 'listings': queryset_listing
        }  
        uid = request.user.id or 0
        return render(request,'listings/search.html',context)
    if request.method == "POST" and "mortagelender" in request.POST:
        print("it issss",request.session['city'])
        keywords = request.session['city']     
        stt = request.session['city']
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+keywords+'&key=AIzaSyCuYOJlcMVw9bYfEw-QNgio7RQVK766-tk')
        lat = r.json()['results'][0]["geometry"]["location"]["lat"]
        lon = r.json()['results'][0]["geometry"]["location"]["lng"]
        lat = str(lat)
        lon = str(lon)
        coordinates = (lat,lon)
        results = rg.search(coordinates)
        state = results[0]['admin1']
        queryset_list = queryset_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state))


        dp_list = dp_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
             | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Down Payment").order_by('id')

        cc_list = cc_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Closing Cost").order_by('id')

        fs_list = fs_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Forgivable Second").order_by('id')

        others_list = others_list.filter(Q(city__iexact=keywords)| Q(state__iexact=keywords)
        | Q(Neighborhoods__iexact=keywords) | Q(Neighborhoods__icontains=keywords)|Q(state__iexact=state )).filter(programtype="Others").order_by('id')

        
        ts = queryset_list.order_by('-participatinglenders')
        amount_of_results = queryset_list.count()  
        paginator = Paginator(ts, 9)   
        page = request.GET.get('page')
        paged_listings = paginator.get_page(page)
        print("lonzg",request.session['lon'])
        print(request.session['link'])
        url = request.session['link']

        context = {
        
            'dplist': dp_list,
            'cclist': cc_list,
            'fslist': fs_list,
            'oplist': others_list,
            'bedroom_choices': bedroom_choices,
            'mapbox_access_token': mapbox_access_token,
            'price_choices': price_choices,
            'listings': paged_listings,
            'my_lon': request.session['lon'],
            'my_lat': request.session['lat'],
            'count': amount_of_results,
            'values': request.session['city'],
            # 'listings': queryset_listing
        }  
        uid = request.user.id or 0
        return render(request,'listings/search.html',context)

    if 'pri' in request.GET:
        keywords = request.GET['price']
        if keywords:
            queryset_list = queryset_list.filter(minimumcontribution__lte=keywords)  
    
    #request.session['lon'] = lon
    # ts = queryset_list.order_by('-programname')
    amount_of_results = queryset_list.count()  
    paginator = Paginator(queryset_list, 9)   
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    print("lonzg",request.session['lon'])
   
  

    context = {
      
        'dplist': dp_list,
        'cclist': cc_list,
        'fslist': fs_list,
        'oplist': others_list,
        'bedroom_choices': bedroom_choices,
        'mapbox_access_token': mapbox_access_token,
        'price_choices': price_choices,
            'listings': paged_listings,
        'my_lon': request.session['lon'],
        'my_lat': request.session['lat'],
        'count': amount_of_results,
        'values': request.session['city'],
        # 'listings': queryset_listing
    }  
    uid = request.user.id or 0
    searchsaved = Searchsave(phrase=request.session['city'],link_visited=request.get_full_path(),length=queryset_list.count(),user_id=request.user.id or 0)
    searchsaved.save()
    return render(request,'listings/search.html',context)