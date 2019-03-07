#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:01:03 2019

@author: Paolo Cozzi <cozzi@ibba.cnr.it>
"""

from django.contrib import admin

from .models import Person

# Register your models here.
admin.site.register(Person, admin.ModelAdmin)
