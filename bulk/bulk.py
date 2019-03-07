#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:10:51 2019

@author: Paolo Cozzi <cozzi@ibba.cnr.it>
"""

from django.conf import settings

from tutorial.models import Person


class Bulk(object):
    def __init__(self, request):
        """
        Initialize the bulk object
        """

        self.session = request.session
        bulk = self.session.get(settings.BULK_SESSION_ID)

        if not bulk:
            # create a new bulk object in the session
            bulk = self.session[settings.BULK_SESSION_ID] = {}

            # create an object in order to store person.id
            bulk['person_ids'] = []

        self.bulk = bulk

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def add(self, item):
        """store item in bulk session"""
        if item not in self.bulk['person_ids']:
            self.bulk['person_ids'].append(item)

            # asserting session update
            self.save()

    def remove(self, item):
        if item in self.bulk['person_ids']:
            self.bulk['person_ids'].remove(item)

            # asserting session update
            self.save()

    def __iter__(self):
        """Iterate through bulk object and returns person item"""

        # get person objects
        persons = Person.objects.filter(id__in=self.bulk['person_ids'])

        for person in persons:
            yield person

    def clear(self):
        """remove bulk from session"""
        del(self.session[settings.BULK_SESSION_ID])
        self.save()

        # and what about my self.bulk attribute?

    def __str__(self):
        return str(self.bulk['person_ids'])
