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


def do_stuff(request):
    if request.method == "POST":
        list_of_ids = request.POST.getlist('check')
        objects = Person.objects.filter(id__in=list_of_ids)
        return render(request, 'tutorial/do_stuff.html', {'objects': objects})
