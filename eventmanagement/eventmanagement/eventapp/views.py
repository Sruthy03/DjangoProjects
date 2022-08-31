from ast import Return
import os
from urllib import request
from django.shortcuts import render,redirect
from eventapp.models import  category,usermember,User,userreg,event
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request,'home.html')

@login_required(login_url='loginpage')
def load_admin_home(request):
    return render(request,'admin/home1.html')

@login_required(login_url='loginpage')
def load_add_category(request):
    return render(request,'admin/add_category.html')

@login_required(login_url='loginpage')
def add_category(request):
    if request.method=='POST':
        eve_name=request.POST['ename']
        eve_food=request.POST['fname']
        eve=category(event_type=eve_name,event_food=eve_food)
        eve.save()
        print('hi')
        return redirect('load_add_category')
    return render(request,'admin/add_category.html')

@login_required(login_url='loginpage')
def load_event(request):
    courses=category.objects.all()
    return render(request,'admin/add_event.html',{'courses':courses})

@login_required(login_url='loginpage')
def add_event(request):
    if request.method=='POST':
        ev_name=request.POST['evt_name']
        ev_des=request.POST['evt_des']
        ev_venue=request.POST['evt_venu']
        ev_people=request.POST['evt_people']
        ev_cost=request.POST['evt_cost']
        if request.FILES.get('photo') is not None:
            photo=request.FILES['photo']
        else:
            photo="static/images/defaultu.jpg"
        sel1=request.POST['sel']
        
        e1=category.objects.get(id=sel1)
        
        evet=event(event_name=ev_name,event_des=ev_des,event_venue=ev_venue,event_people=ev_people,event_cost=ev_cost,event_photo=photo,category=e1)
        evet.save()
        print('hi')
        return redirect('load_event')
    return render(request,'admin/add_event.html')

def loginpage(request):
    return render(request,'login.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('load_admin_home')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'welcome {username}')
                return redirect('load_user_home')
        else:
            messages.info(request,"invalid username or password")
            return redirect('loginpage')
    return render(request,'home.html')

@login_required(login_url='load_signup')
def load_user_home(request):
    return render(request,'user/home2.html')

def load_signup(request):
    return render(request,'signup.html')

def u_signup(request):
    if request.method=='POST':
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        address=request.POST.get('adname')
        email=request.POST.get('email')
        uname=request.POST.get('username')
        pname=request.POST.get('password')
        cname=request.POST.get('cpassword')
        gender=request.POST.get('gender')
        mobilee=request.POST.get('mname')
        if request.FILES.get('photo') is not None:
            photo=request.FILES['photo']
        else:
            photo="static/images/default.png"
        if cname==pname:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'username not available')
                return redirect('load_signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email not available')
                return redirect('load_signup')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,password=pname,username=uname,email=email)
                user.save()
                u=User.objects.get(id=user.id)
                member=usermember(user_address=address,user_gender=gender,user_mobile=mobilee,user_photo=photo,user=u)
                member.save()
                return redirect('loginpage')
    return render(request,'signup.html')

@login_required(login_url='load_signup')
def show_events(request):
    context=event.objects.all()
    return render(request,'user/show_events.html',{'dataread':context})

@login_required(login_url='load_signup')
def load_registration(request):
    courses=category.objects.all()
    return render(request,'user/registration.html',{'courses':courses})

@login_required(login_url='load_signup')
def register(request):
    if request.method=='POST':
        u_name=request.POST['name']
        u_ads=request.POST['aname']
        u_email=request.POST['ename']
        u_cno=request.POST['cname']
        u_sdate=request.POST['sdate']
        u_edate=request.POST['edate']
        u_pno=request.POST['pname']
        cel1=request.POST['cel']
        
        u1=category.objects.get(id=cel1)
        
        reg=userreg(user_name=u_name,user_adres=u_ads,user_email=u_email,user_cno=u_cno,user_sdate=u_sdate,user_edate=u_edate,user_people=u_pno,category=u1)
        reg.save()
        print('hi')
        return redirect('load_user_home')
    return render(request,'user/registration.html')

@login_required(login_url='loginpage')
def show_bookings(request):
    c=userreg.objects.all()
    return render(request,'admin/show_bookings.html',{'c':c})

@login_required(login_url='loginpage')
def show_event(request):
    context=event.objects.all()
    return render(request,'admin/show_event.html',{'d':context})

@login_required(login_url='loginpage')
def delete(request,pk):
    st=event.objects.get(id=pk)
    st.delete()
    return redirect('show_event')

@login_required(login_url='loginpage')
def edit_page(request,pk):
    e=event.objects.get(id=pk)
   
    return render(request,'admin/edit.html',{'e':e})

@login_required(login_url='loginpage')
def edit_details(request,pk):
    if request.method=='POST':
        e=event.objects.get(id=pk)
        e.event_name=request.POST.get('ename')
    
        e.event_des=request.POST.get('dname')
        e.event_people=request.POST.get('pname')
        
        e.event_cost=request.POST.get('cname')
       
       
        e.save()
        
        return redirect('show_event')
    return render(request,'admin/edit.html')

@login_required(login_url='loginpage')
def admin_logout(request):
    auth.logout(request)
    return render(request,'home.html')

@login_required(login_url='load_signup')
def user_logout(request):
    auth.logout(request)
    return render(request,'home.html')

@login_required(login_url='load_signup')
def card(request,pk):
    users=event.objects.get(id=pk)
    return render(request,'user/card.html',{'users':users})

def about(request):
    return render(request,'about.html')

def gallary(request):
    return render(request,'gallary.html')


def contact(request):
    return render(request,'contact.html')

def d(request):
    return render(request,'admin/d.html')

def navbar(request):
    return render(request,'user/navbar.html')


@login_required(login_url='loginpage')
def remove(request,pk):
    st=userreg.objects.get(id=pk)
    st.delete()
    return redirect('show_bookings')