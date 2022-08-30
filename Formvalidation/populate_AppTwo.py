import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random

from AppTwo.models import Users
from faker import Faker

fakegen=Faker()

# topics =['Search','Social','MarketPlace','News','Games']

# def add_topic():
#     t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
#     t.save()
#     return t

def populate(N = 5):
    for elemn in range(N):
        fake_fname = fakegen.name()
        fake_lname =fakegen.name()
        fake_email = fakegen.email()
      

        users_obj= Users.objects.get_or_create(fname= fake_fname,lname=fake_lname,email=fake_email)[0]

if __name__ == '__main__':
    print("populating")
    populate(20)
    print("populating completed!")
