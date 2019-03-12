from django.shortcuts import render
from django_tables2 import SingleTableView, RequestConfig
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.db.models import Value, CharField, F, BooleanField, ExpressionWrapper, Func, When

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

#    def get_queryset(self):
#        bulk = Bulk(self.request)
#        print(bulk)
#        queryset = super(PersonList, self).get_queryset()
#        # queryset = queryset.annotate(miao=Value('Miao', CharField()))
#        queryset = queryset.annotate(
#            miao=ExpressionWrapper(
#                Value(F('id')),
#                output_field=CharField()
#            )
#        )
#
#        for item in queryset:
#            print(item.miao)
#
#        return queryset

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

        # determine if I have already called this instance or not
        if 'update' not in request.POST:
            context = self.get_context_data()
            print(context)
            print(type(context['form']))
            return self.render_to_response(context)

        form = self.get_form()
        form.is_valid()

        print(request.POST)
        print(self.get_form_kwargs())
        print("Called my post")
        print(form)
        print(type(form))
        print(form["update"].value())
        print(form.cleaned_data["update"])
        print(form.is_valid())

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
