from django.urls import path,include
from AppTwo import views

urlpatterns=[
   
    path("",views.Users,name="Users"),
    path("",views.help,name="help"),

]