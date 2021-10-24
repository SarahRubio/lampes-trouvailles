import re
import operator

from django import forms
from django.db.models import Q, F
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import FilteredSelectMultiple

from filters.models import Category, SubCategory, Color, Designer, Material, State, Style


class ObjectSearchForm(forms.Form):
    """Main form for search engine."""

    SUBCATEGORIES_QS = SubCategory.objects \
        .select_related('category') \
        .order_by('category__name', 'name')

    categories = forms.ModelMultipleChoiceField(
        label='Catégories',
        queryset=Category.objects.all(),
        to_field_name='slug',
        required=False,
        widget=forms.CheckboxSelectMultiple)
    subcategories = forms.ModelMultipleChoiceField(
        label='Catégories',  # Not a mistake
        queryset=SUBCATEGORIES_QS,
        to_field_name='slug',
        required=False,
         widget=forms.CheckboxSelectMultiple)
    is_negotiable = forms.BooleanField(
        label='prix négociable',
        required=False)
    price_min = forms.IntegerField(
        label='min',
        required=False)
    price_max = forms.IntegerField(
        label='max',
        required=False)
    designers = forms.ModelMultipleChoiceField(
        label="Designer",
        queryset=Designer.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple)
    state = forms.ModelMultipleChoiceField(
        label="état",
        queryset=State.objects.all(),
        to_field_name='slug',
        required=False,
        widget=forms.CheckboxSelectMultiple)
    materials = forms.ModelMultipleChoiceField(
        label="Matériaux",
        queryset=Material.objects.all(),
        to_field_name='slug',
        required=False,
        widget=forms.CheckboxSelectMultiple)
    style = forms.ModelMultipleChoiceField(
        label="Style",
        queryset=Style.objects.all(),
        to_field_name='slug',
        required=False,
        widget=forms.CheckboxSelectMultiple)
    colors = forms.ModelMultipleChoiceField(
        label='Couleurs',
        required=False,
        queryset=Color.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    def filter_queryset(self, qs=None):
        """Filter querysets depending of input data."""

        # If no qs was passed, just start with all published aids
        if qs is None:
            qs = Light.objects.all()

        if not self.is_bound:
            return qs

        # Populate cleaned_data
        if not hasattr(self, 'cleaned_data'):
            self.full_clean()

        is_negotiable= self.cleaned_data.get('is_negotiable', False)
        if is_negotiable:
            qs = qs.filter(is_negotiable=True)

        subcategories = self.cleaned_data.get('subcategories', None)
        if subcategories:
            qs = qs.filter(subcategories__in=subcategories)

        designers = self.cleaned_data.get('designers', None)
        if designers:
            qs = qs.filter(designer__in=designers)

        materials = self.cleaned_data.get('materials', None)
        if materials:
            qs = qs.filter(materials__in=materials)

        price_min = self.cleaned_data.get('price_min', 0)
        price_max = self.cleaned_data.get('price_max', None)
        if price_min or price_max:
            if not price_min:
                self.cleaned_data['price_min'] = 0
                price_min = self.cleaned_data['price_min']
                qs = qs.filter(price__range=(price_min, price_max))
            if not price_max:
                self.cleaned_data['price_max'] = 999999
                price_max = self.cleaned_data['price_max']
                qs = qs.filter(price__range=(price_min, price_max))
            else:
                qs = qs.filter(price__range=(price_min, price_max))

        state = self.cleaned_data.get('state', None)
        if state:
            qs = qs.filter(state__in=state)

        style = self.cleaned_data.get('style', None)
        if style:
            qs = qs.filter(style__in=style)

        colors = self.cleaned_data.get('colors', None)
        if colors:
            qs = qs.filter(colors__in=colors)

        # We filter by theme only if no categories were provided.
        # This is to handle the following edge case: on the multi-step search
        # form, the user selects a category, then on the last step, doesn't select
        # any subcategories and just click "Search".
        categories = self.cleaned_data.get('categories', None)
        if categories and not subcategories:
            qs = qs.filter(subcategories__categories__in=categories)

        return qs
