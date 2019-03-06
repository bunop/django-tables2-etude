#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:36:24 2019

@author: Paolo Cozzi <cozzi@ibba.cnr.it>
"""

from django.conf.urls import url
from . import views

app_name = 'bulk'

urlpatterns = [
    url(r'^$', views.bulk_detail, name='bulk_detail'),
    url(r'add/(?P<pk>[-\w]+)/$',
        views.bulk_add,
        name='bulk_add'),
    url(r'remove/(?P<pk>[-\w]+)/$',
        views.bulk_remove,
        name='bulk_remove'),
]
