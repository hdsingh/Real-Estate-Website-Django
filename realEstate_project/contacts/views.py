from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact = Contact(listing_id = listing_id,
                            listing = listing,
                            name = name,
                            email = email,
                            phone = phone,
                            message = message,
                            user_id =user_id,)
        contact.save()
        
        messages.success(request,"Your request has been submitted. "+
        "We will get backto you soon.")
        
        return redirect('/listing/'+listing_id)