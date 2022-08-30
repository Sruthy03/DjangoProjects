from django.urls import path,include
from user.views import index,logout,login,register,home

urlpatterns=[
    path("",index,name="index"),
    path("home",home,name="home"),
     path("logout",logout,name="logout"),
      path("login",login,name="login"),
       path("register",register,name="register"),
]