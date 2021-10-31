from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from objects.models import Light, Finding, Furniture
from objects.forms import ObjectSearchForm
from filters.models import Color


class SearchView(FormMixin, ListView):
    """Search and display objects."""

    form_class = ObjectSearchForm

    def get(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.form.full_clean()
        self.store_current_search()
        return super().get(request, *args, **kwargs)

    def get_form_kwargs(self):
        """Take input data from the GET values."""
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.request.GET,
        })
        return kwargs

    def store_current_search(self):
        """Store the current search query in a cookie.

        This is needed to provide the correct "go back to your search" link in
        other pages' breadcrumbs.
        """
        current_search_query = self.request.GET.urlencode()
        self.request.session['SEARCH_COOKIE_NAME'] = current_search_query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['current_search'] = self.request.session.get('SEARCH_COOKIE_NAME', '')
        context['colors'] = Color.objects.all()

        return context


class LightList(SearchView):
    template_name = 'lights/lights_list.html'
    context_object_name = 'lights'
    paginate_by = 18
    form_class = ObjectSearchForm

    def get_queryset(self):
        """Return the list of results to display."""

        qs = Light.objects \
            .prefetch_related('designer') \
            .prefetch_related('categories') \
            .prefetch_related('subcategories') \
            .prefetch_related('style') \
            .prefetch_related('materials') \
            .prefetch_related('colors') \
            .prefetch_related('state')

        filter_form = self.form
        results = filter_form.filter_queryset(qs).distinct()

        return results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_products'] = Light.objects.all()[:5]

        return context
    

class LightDetail(DetailView):
    template_name = 'lights/lights_detail.html'
    context_object_name = 'light'
    queryset = Light.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FindingList(SearchView):
    template_name = 'findings/findings_list.html'
    context_object_name = 'findings'
    paginate_by = 18
    form_class = ObjectSearchForm

    def get_queryset(self):
        """Return the list of results to display."""

        qs = Finding.objects \
            .prefetch_related('designer') \
            .prefetch_related('categories') \
            .prefetch_related('subcategories') \
            .prefetch_related('style') \
            .prefetch_related('materials') \
            .prefetch_related('colors') \
            .prefetch_related('state')

        filter_form = self.form
        results = filter_form.filter_queryset(qs).distinct()

        return results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_products'] = Finding.objects.all()[:5]

        return context


class FindingDetail(DetailView):
    template_name = 'findings/findings_detail.html'
    context_object_name = 'finding'
    queryset = Finding.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FurnitureList(SearchView):
    template_name = 'furnitures/furnitures_list.html'
    context_object_name = 'furnitures'
    paginate_by = 18
    form_class = ObjectSearchForm

    def get_queryset(self):
        """Return the list of results to display."""

        qs = Furniture.objects \
            .prefetch_related('designer') \
            .prefetch_related('categories') \
            .prefetch_related('subcategories') \
            .prefetch_related('style') \
            .prefetch_related('materials') \
            .prefetch_related('colors') \
            .prefetch_related('state')

        filter_form = self.form
        results = filter_form.filter_queryset(qs).distinct()

        return results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_products'] = Furniture.objects.all()[:5]

        return context


class FurnitureDetail(DetailView):
    template_name = 'furnitures/furnitures_detail.html'
    context_object_name = 'furniture'
    queryset = Furniture.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
