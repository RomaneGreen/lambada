from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.

def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST.get['user_id']
    lender_email = request.POST['lender_email']
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
      if has_contacted:
        messages.error(request,'You have already made an inquiry for this listing')
        return redirect('/listings/'+listing_id)

    contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
    
    contact.save()

    send_mail (
        'Lambada listing inquiry',
        'There has been a inquire for ' + listing +  '. sign into the admin panel for more info',
        'lambadalambadatest@gmail.com',
        [lender_email,'romane71193@gmail.com'],
        fail_silently = False
    )
    messages.success(request,'Your request has been sent and saved to your dashboard')
    return redirect('/listings/'+listing_id)

    return
        
 
