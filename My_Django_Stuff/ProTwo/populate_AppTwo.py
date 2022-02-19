import os
from re import T
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for N in range(N):
        fake_fullname = fakegen.name().split(" ")
        fake_first_name = fake_fullname[0]
        fake_last_name = fake_fullname[1]

        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_first_name, 
            last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(4)
    print("Populating Complete")


