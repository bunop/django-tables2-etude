#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:21:07 2019

@author: Paolo Cozzi <cozzi@ibba.cnr.it>
"""

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.http import HttpResponseBadRequest


def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()

        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__

    return wrap


# https://stackoverflow.com/a/13409704/4385116
class AjaxGeneral(TemplateView):
    template_name = None

    def get(self, request):
        data = {}

        return render_to_response(
            self.template_name, data,
            context_instance=RequestContext(request))

    @method_decorator(ajax_required)
    def dispatch(self, *args, **kwargs):
        return super(AjaxGeneral, self).dispatch(*args, **kwargs)
