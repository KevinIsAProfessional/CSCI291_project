from django.shortcuts import render
from django.views.generic import TemplateView

class CypherPageView(TemplateView):
    template_name = 'cypher/cypher.html'

class CaesarPageView(TemplateView):
    template_name = 'cypher/caesar.html'
