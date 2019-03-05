from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Person
from .tables import PersonTable


def people(request):
    table = PersonTable(Person.objects.all())

    # Using RequestConfig automatically pulls values from request.GET and
    # updates the table accordingly. This enables data ordering and pagination.
    RequestConfig(request).configure(table)
    return render(request, 'tutorial/people.html', {'table': table})
