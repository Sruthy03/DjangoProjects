from django.shortcuts import render,redirect
from user.forms import UserRegistrtionForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

# Create your views here.
def index(request):
    return render(request,'user/index.html')
def home(request):
    return render(request,'user/home.html')
def logout(request):
    auth_logout(request)
    return render(request,'user/index.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password=password)
        if user is not None:
            form = auth_login(request, user)
            return redirect('home')
        else:
            form = AuthenticationForm()
            return render(request,'user/login.html',{"login_form":form})
    else:
        form = AuthenticationForm()
        return render(request,'user/login.html',{"login_form":form})

    
def register(request):

    
    if request.method == "POST":
        form = UserRegistrtionForm(request.POST)
        if form.is_valid():
            user= form.save()
            # login(request,user)
            messages.success(request, "Registration successful." )
            return redirect('login')
        else:
            messages.success(request, "Registration unsuccessful." )
            return redirect(request,"user/register.html",{'register_form':form})


    else:
        form = UserRegistrtionForm()
        return render(request,"user/register.html",{'register_form':form})


