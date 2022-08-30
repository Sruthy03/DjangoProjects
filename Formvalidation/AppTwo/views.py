from django.shortcuts import render
from AppTwo.forms import NewUserForm
#from django.http import HttpResponse
#from AppTwo.models import Users
# Create your views here.

def index(request):
     return render(request,'AppTwo/index.html')

def help(request):
    help_dict={'help_page':"HelpPage"}
    return render(request,'AppTwo/index.html',context=help_dict)

def Users(request):
     form = NewUserForm()

     if request.method == "POST":
          form = NewUserForm(request.POST)

          if form.is_valid():
               form.save(commit=True)
               return index(request)
     return render(request,'AppTwo/user.html',{'form':form})
     

# def userlist(request):
#      users_list = Users.objects.order_by('fname')
#      user_dict ={'users':users_list}
#      return render(request,'AppTwo/user.html',context=user_dict)
