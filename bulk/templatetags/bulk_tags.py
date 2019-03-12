#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:22:01 2019

@author: Paolo Cozzi <cozzi@ibba.cnr.it>
"""

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def is_checked(context, person_id):
    person_ids = context['person_ids']
    print(person_id)
    print(person_ids)
    if person_id in person_ids:
        return mark_safe("checked")
