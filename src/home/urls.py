from django.urls import path
from django.views.generic import TemplateView

from home.views import HomeView, AboutView, HowView, ContactView, LegalMentionsView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('how/', HowView.as_view(), name='how'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('legal-mentions/', LegalMentionsView.as_view(), name='legal-mentions'),
]