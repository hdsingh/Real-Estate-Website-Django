from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.
def dashboard(request):
    user_contacts = Contact.objects.filter(user_id = request.user.id).order_by('-contact_date')

    context = {
        'contacts': user_contacts,
    }
    return render(request,'accounts/dashboard.html',context)

def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username = username,password = password)

       if user:
          auth.login(request,user)
          messages.success(request,"You are now logged in.")
          return redirect('dashboard')
       else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')       
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"Logged Out")
    return redirect("index")

def register(request):
    if request.method == "POST":
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username = username).exists():
                messages.error(request,"That username is taken.")
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request,"That email is taken.")
                    return redirect('register')
                else:
                    # looks good
                    user = User.objects.create_user(username = username,
                    password = password,email=email,first_name = first_name,
                    last_name = last_name)
                    user.save()
                    # Login after register
                    auth.login(request,user)
                    messages.success(request,"You are now logged in.")
                    return redirect('index')

                    # # Login manually 
                    # messages.success(request,"You can now log in.")
                    # return redirect('login')
        else:
            messages.error(request,'Passwords do not match.')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

