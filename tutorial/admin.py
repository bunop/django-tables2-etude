#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:01:03 2019

@author: Paolo Cozzi <cozzi@ibba.cnr.it>
"""

from django.contrib import admin

from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_per_page = 25


# Register your models here.
admin.site.register(Person, PersonAdmin)
