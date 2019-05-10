#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:29:57 2019

@author: Paolo Cozzi <cozzi@ibba.cnr.it>
"""

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.decorators.http import require_POST
from tutorial.models import Person

from common.decorators import ajax_required, AjaxGeneral

from .bulk import Bulk


@ajax_required
@require_POST
def bulk_add(request):
    bulk = Bulk(request)
    person_id = request.POST.get('person_id')

    try:
        person = Person.objects.get(pk=person_id)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'ko'})

    # update bulk object
    bulk.add(person.id)

    return JsonResponse({'status': 'ok'})


#@ajax_required
#@require_POST
#def bulk_remove(request):
#    bulk = Bulk(request)
#    person_id = request.POST.get('person_id')
#
#    try:
#        person = Person.objects.get(pk=person_id)
#
#    except ObjectDoesNotExist:
#        return JsonResponse({'status': 'ko'})
#
#    # update bulk object
#    bulk.remove(person.id)
#
#    return JsonResponse({'status': 'ok'})

# sample implementation using CBV
class BulkRemoveView(AjaxGeneral):
    # forcing POST methods only
    # https://stackoverflow.com/a/36865283/4385116
    http_method_names = ['post']

    def post(self, request):
        bulk = Bulk(self.request)
        person_id = self.request.POST.get('person_id')

        try:
            person = Person.objects.get(pk=person_id)

        except ObjectDoesNotExist:
            return JsonResponse({'status': 'ko'})

        # update bulk object
        bulk.remove(person.id)

        return JsonResponse({'status': 'ok'})


# TODO: need to customize response relying on parameters received
@ajax_required
@require_POST
def bulk_list(request):
    bulk = Bulk(request)

    page = request.POST.get('page')
    print("Page: %s" % (page))
    print(request)
    print(request.user)

    # get all persons id
    response = bulk.bulk["person_ids"]

    return JsonResponse({"person_ids": response})


def bulk_detail(request):
    bulk = Bulk(request)
    return render(request, 'bulk/detail.html', {'bulk': bulk})
