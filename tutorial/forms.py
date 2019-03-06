#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:50:50 2019

@author: Paolo Cozzi <cozzi@ibba.cnr.it>
"""

from django import forms


class InfoForm(forms.Form):
#    check = forms.MultipleChoiceField(
#        # choices = LIST_OF_VALID_CHOICES, # this is optional
#        widget=forms.CheckboxSelectMultiple,
#    )

    info = forms.CharField()
    update = forms.BooleanField(widget=forms.HiddenInput, required=False)
