from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class category(models.Model):
    event_type=models.CharField(max_length=255)
    event_food=models.CharField(max_length=255,null=True)


class event(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    event_name=models.CharField(max_length=255)
    event_des=models.CharField(max_length=255)
    event_venue=models.CharField(max_length=255)
    event_people=models.IntegerField()
    event_cost=models.IntegerField()
    event_photo=models.ImageField(upload_to="image/",null=True)
    

class usermember(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    user_address=models.CharField(max_length=255)
    user_gender=models.CharField(max_length=255)
    user_mobile=models.CharField(max_length=255)
    user_photo=models.ImageField(upload_to="image/",null=True)

class userreg(models.Model):
    
    category=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    user_name=models.CharField(max_length=255)
    user_email=models.EmailField()
    user_cno=models.CharField(max_length=255)
    user_sdate=models.DateField()
    user_edate=models.DateField()
    user_people=models.IntegerField(null=True)
    user_adres=models.CharField(max_length=200,null=True)








