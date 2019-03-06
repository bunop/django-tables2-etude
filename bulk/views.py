#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:29:57 2019

@author: Paolo Cozzi <cozzi@ibba.cnr.it>
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from tutorial.models import Person

from .bulk import Bulk


@require_POST
def bulk_add(request, person_id):
    bulk = Bulk(request)
    person = get_object_or_404(Person, id=person_id)

    # update bulk object
    bulk.add(person.id)

    return redirect('bulk:bulk_detail')


@require_POST
def bulk_remove(request, person_id):
    bulk = Bulk(request)
    person = get_object_or_404(Person, id=person_id)

    # update bulk object
    bulk.remove(person.id)

    return redirect('bulk:bulk_detail')


def bulk_detail(request):
    bulk = Bulk(request)
    return render(request, 'bulk/detail.html', {'bulk': bulk})
