#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:26:07 2019

@author: Paolo Cozzi <cozzi@ibba.cnr.it>
"""

import django_tables2 as tables
from .models import Person


# While simple, passing a QuerySet directly to {% render_table %} does not
# allow for any customization. For that, you must define a custom Table class:
class PersonTable(tables.Table):

    check = tables.CheckBoxColumn(accessor="pk")

    class Meta:
        model = Person
        template_name = 'django_tables2/bootstrap.html'
