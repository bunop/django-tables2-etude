from django.shortcuts import render
from django_tables2 import SingleTableView, RequestConfig
from .models import Person
from .tables import PersonTable


class PersonList(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = "tutorial/people.html"

    def post(self, request, *args, **kwargs):
        list_of_ids = request.POST.getlist('check')
        objects = Person.objects.filter(id__in=list_of_ids)
        table = PersonTable(objects)
        RequestConfig(request).configure(table)
        return render(request, self.template_name, {'table': table})
