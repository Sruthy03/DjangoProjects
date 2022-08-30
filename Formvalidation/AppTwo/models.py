from django.db import models

# Create your models here.

class Users(models.Model):
    fname = models.CharField(max_length=254)
    lname = models.CharField(max_length=254)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.fname+self.lname