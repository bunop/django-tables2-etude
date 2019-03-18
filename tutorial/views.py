from django.shortcuts import render
from django_tables2 import SingleTableView, RequestConfig
from django.views.generic import FormView
from django.urls import reverse_lazy

from bulk.bulk import Bulk

from .models import Person
from .tables import PersonTable
from .forms import InfoForm


class PersonList(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = "tutorial/people.html"
    paginate_by = 15
    ordering = ["id"]

    def post(self, request, *args, **kwargs):
        list_of_ids = request.POST.getlist('check')
        objects = Person.objects.filter(id__in=list_of_ids)
        table = PersonTable(objects)
        RequestConfig(request).configure(table)
        return render(request, self.template_name, {'table': table})

    def get_context_data(self, **kwargs):
        context = super(PersonList, self).get_context_data(**kwargs)
        bulk = Bulk(self.request)
        context['person_ids'] = bulk.bulk['person_ids']
        return context


class BulkUpdate(FormView):
    form_class = InfoForm
    template_name = "tutorial/bulk_update.html"
    success_url = reverse_lazy('people')

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """

        form = self.get_form()
        bulk = Bulk(request)

        if form.is_valid():
            info = form.cleaned_data["info"]
            for person in bulk:
                person.info = info
                person.save()

            # clear bulk object
            bulk.clear()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)
