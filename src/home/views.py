from django.shortcuts import render
from django.views.generic import TemplateView
from objects.models import Light


class HomeView(TemplateView):
    
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_products'] = Light.objects.all()[:5]
        return context


class HowView(TemplateView):
    
    template_name = 'home/how.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class AboutView(TemplateView):
    
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class ContactView(TemplateView):
    
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class LegalMentionsView(TemplateView):
    
    template_name = 'home/legal_mentions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
