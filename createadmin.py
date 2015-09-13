#!/usr/bin/env python

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinesend.settings")
import django

django.setup()

from django.contrib.auth.models import User, Group

if User.objects.count() == 0:
    bitcine_staff = Group(name="BitCine Founders Team")
    bitcine_staff.save()

    keyvan = User.objects.create_user('keyvan', 'keyvan@bitcine.com', 'password')
    keyvan.first_name = "Keyvan"
    keyvan.last_name = "Mosharraf"
    keyvan.is_superuser = True
    keyvan.is_staff = True
    keyvan.save()
    keyvan.groups.add(bitcine_staff)

    jeff = User.objects.create_user('jeff', 'jeff@bitcine.com', 'password')
    jeff.first_name = "Jeff"
    jeff.last_name = "Gingras"
    jeff.is_staff = True
    jeff.save()
    jeff.groups.add(bitcine_staff)

    colin = User.objects.create_user('colin', 'colin@bitcine.com', 'password')
    colin.first_name = "Colin"
    colin.last_name = "Carter"
    colin.is_staff = True
    colin.save()
    colin.groups.add(bitcine_staff)
