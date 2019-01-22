import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DjangoModelForm.settings')

import django
django.setup()


## FAKE POP Script

import random
from ProTwo.models import *
from faker import Faker

fakegen=Faker()


def populate(N=5):
    ## get the topic for the entry
    for entry in range(N):


        fake_name=fakegen.name().split()
        fake_first_name=fake_name[0]
        fake_last_name = fake_name[1]
        fake_email=fakegen.email()

        #Entry
        user=User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]


if __name__ =='__main__':
    print("Populating script!")
    populate(20)
    print("Populating complete")


