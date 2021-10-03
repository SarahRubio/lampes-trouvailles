from django.shortcuts import render
from django.views.generic import ListView, DetailView

from objects.models import Light, Finding, Furniture


class LightList(ListView):
    template_name = 'lights/lights_list.html'
    context_object_name = 'lights'
    paginate_by = 18

    def get_queryset(self):
        qs = Light.objects.all()
        return qs


class LightDetail(DetailView):
    template_name = 'lights/lights_detail.html'
    context_object_name = 'light'
    queryset = Light.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FindingList(ListView):
    template_name = 'findings/findings_list.html'
    context_object_name = 'findings'
    paginate_by = 18

    def get_queryset(self):
        qs = Finding.objects.all()
        return qs


class FindingDetail(DetailView):
    template_name = 'findings/findings_detail.html'
    context_object_name = 'finding'
    queryset = Finding.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FurnitureList(ListView):
    template_name = 'furnitures/furnitures_list.html'
    context_object_name = 'furnitures'
    paginate_by = 18

    def get_queryset(self):
        qs = Furniture.objects.all()
        return qs


class FurnitureDetail(DetailView):
    template_name = 'furnitures/furnitures_detail.html'
    context_object_name = 'furniture'
    queryset = Furniture.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
