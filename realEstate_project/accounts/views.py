from django.shortcuts import render, redirect

# Create your views here.
def dashboard(request):
    return render(request,'accounts/dashboard.html')

def login(request):
    if request.method == "POST":
        return 
    else:
        return render(request,'accounts/login.html')

def logout(request):
    return redirect("index")

def register(request):
    if request.method == 'POST':
        return redirect('index')
    else:
        return render(request,'accounts/register.html')

