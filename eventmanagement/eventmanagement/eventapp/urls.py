from . import views
from django.urls import path,include

urlpatterns = [

    path('',views.homepage,name='homepage'),
    path('load_admin_home',views.load_admin_home,name='load_admin_home'),
    path('load_add_category',views.load_add_category,name='load_add_category'),
    path('add_category',views.add_category,name='add_category'),
    path('load_event',views.load_event,name='load_event'),
    path('add_event',views.add_event,name='add_event'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('load_user_home',views.load_user_home,name='load_user_home'),
    
    path('user_login',views.user_login,name='user_login'),
    path('load_signup',views.load_signup,name='load_signup'),
    path('u_signup',views.u_signup,name='u_signup'),
    path('show_events',views.show_events,name='show_events'),
    path('load_registration',views.load_registration,name='load_registration'),
    path('register',views.register,name='register'),
    path('show_bookings',views.show_bookings,name='show_bookings'),
    path('show_event',views.show_event,name='show_event'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit_page/<int:pk>',views.edit_page,name='edit_page'),
    path('edit_details/<int:pk>',views.edit_details,name='edit_details'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('card/<int:pk>',views.card,name='card'),
    path('about',views.about,name='about'),
    path('gallary',views.gallary,name='gallary'),
    
    path('contact',views.contact,name='contact'),
    path('d',views.d,name='d'),
    path('navbar',views.navbar,name='navbar'),
    path('remove/<int:pk>',views.remove,name='remove'),
]