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
    url(r'^$', views.bulk_detail, name='detail'),
    url(r'add/$',
        views.bulk_add,
        name='add'),
    url(r'remove/$',
        views.BulkRemoveView.as_view(),
        name='remove'),
    url(r'list/$',
        views.bulk_list,
        name='list'),
]
