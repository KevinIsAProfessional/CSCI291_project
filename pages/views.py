# pages/views.py

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class ConstructionPageView(TemplateView):
    template_name = 'construction.html'

class CypherPageView(TemplateView):
    template_name = 'cypher.html'
