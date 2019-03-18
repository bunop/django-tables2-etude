#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:50:50 2019

@author: Paolo Cozzi <cozzi@ibba.cnr.it>
"""

from django import forms


class InfoForm(forms.Form):
    info = forms.CharField()
