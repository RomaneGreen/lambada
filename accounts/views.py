from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
from listings.models import Searchsave
from listings.models import Listing
from accounts.models import UserProfile
from django.contrib.gis.geoip2 import GeoIP2
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import requests
import ipinfo


# Create your views here.
def register(request):
  if request.method == "POST":

    fullname = request.POST['fullname']
    email = request.POST['email']
    password = request.POST['password']
    passowrd2 = request.POST['password2']
    username = request.POST['username']
    # occupation = request.POST['occupation']
    # employer = request.POST['employer']
    # income = request.POST['income']
    # familysize = request.POST['familysize']
     
    if password == passowrd2:
      if User.objects.filter(username=username).exists():
        messages.error(request,'That username is taken')
        return redirect('register')
      else:
         if User.objects.filter(email=email).exists():
           messages.error(request,'That email is being used')
           return redirect('register')
         else:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=fullname,last_name=fullname)
            #fullname=fullname,occupation=occupation,employer=employer,income=income,familysize=familysize)
            # To login after register
            # auth.login(request,user)
            # messages.success(request,'You are now logged in')
            # return redirect('index')
            user.save()
            print(user,user.id,user.username)
            # test = User.objects.get(id=user.id)
            request.session['user'] = user.id
           # messages.success(request,'You are now registered and can log in')
            return redirect('enroll')
             
    else:
      messages.error(request, 'Passwords do not match')      
      return redirect('register')
  else:
    return render(request,'accounts/register.html')


def login(request):
  if request.method == "POST":
     username = request.POST['username']
     password = request.POST['password']
    #Login user
     user = auth.authenticate(username=username,password=password)
     if user is not None:
       auth.login(request,user)
       messages.success(request,'You are now logged in')
       return redirect('dashboard')
     else:
       messages.error(request,'Invalid Credentials')
       return redirect('login')
  else:
    return render(request,'accounts/login.html')
    


def logout(request):
  if request.method == "POST":
     auth.logout(request)
     messages.success(request,'You are now logged out')
     return redirect('index')


def dashboard(request):
  access_token = 'bcd68a7fad37ec'
  handler = ipinfo.getHandler(access_token)
  ipinfos = '50.205.13.0'
  details = handler.getDetails(ipinfos)
  citiez =  details.all
  #ipinfo = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
  listings = Listing.objects.order_by('id')
  searches = Searchsave.objects.filter(user_id=request.user.id)
  #count = Searchsave.length()
  #r = requests.get('https://www.iplocate.io/api/lookup/'+ipinfo)
  #city = r.json()['city']
  #print(r.json()['city'])

  paginator = Paginator(user_contacts, 6)
  page = request.GET.get('page')
  user_contacts = paginator.get_page(page)

  paginator = Paginator(searches, 6)
  page = request.GET.get('page')
  searches = paginator.get_page(page)

  context = {
    'contacts' : user_contacts,
    'listings': listings,
   # 'city': city,
    'citiez': citiez,
    'searches': searches,
    #'count' : count
   
  }
  return render(request,'accounts/dashboard.html', context)



def search_delete(request,search_id):
  # s = get_object_or_404(Searchsave, id=search_id)
  s=Searchsave.objects.filter(id=search_id)
  s.delete()
  print("heyyyyy",)
  return redirect('/accounts/dashboard')
  return

def enroll(request):
  print("Watch",request.session['user'])
  usa = request.session['user']
  user = User.objects.get(id=usa)
  print("USA",user)
  if request.method == "POST":
     print("hallo") 
     occupation = request.POST['occupation']
     employer = request.POST['employer']
     familysize = request.POST['familysize']
     annualincome = request.POST['annualincome']
     print(occupation,employer,familysize,annualincome)
     userProfile = UserProfile.objects.create(occupation=occupation,employer=employer,familysize=familysize,householdincome=annualincome,user=user)
     userProfile.save()
     messages.success(request,'You are can now in')
     return redirect('index')
    #  return render(request,'accounts/dashboard.html')
  else:
    # user = request.user
    return render(request,'accounts/enroll.html')
     

  
  return render(request,'accounts/enroll.html')


def enrolled(request):
  print("hallo",request.session['user']) 
  if request.method == "POST":
     print("hallo",request.session['user']) 
     occupation = request.POST['occupation']
     employer = request.POST['employer']
     familysize = request.POST['familysize']
     annualincome = request.POST['annualincome']
     user = request.user
     print(occupation,employer,familysize,annualincome)
    #  UserProfile = UserProfile.objects.create_user(username=username,password=password,email=email,first_name=fullname,last_name=fullname)
    #  userProfile = UserProfile.objects(occupation=occupation,employer=employer,familysize=familysize,householdincome=annualincome,user=user)
     userProfile = UserProfile.objects.filter(user=user).update(occupation=occupation,employer=employer,familysize=familysize,householdincome=annualincome,user=user)
     profile = UserProfile.objects.get(user=user)
     print(profile)
     context = {
    'profile' : profile,
  }
    #  userProfile.save()

     return render(request,'accounts/enrolled.html',context)
  else:
    print("hallo",request.session['user']) 
    user = request.user
    profile = UserProfile.objects.get(user=user)
    print(profile)
    context = {
    'profile' : profile,
  }
    return render(request,'accounts/enrolled.html',context)
     
