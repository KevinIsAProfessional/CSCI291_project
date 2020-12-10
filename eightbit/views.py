from django.shortcuts import render
from django.views.generic import TemplateView 

class EightBitPageView(TemplateView):
    template_name = 'eightbit/eightbit.html'

class ClockPageView(TemplateView):
    template_name = 'eightbit/clock.html'

class RegistersPageView(TemplateView):
    template_name = 'eightbit/registers.html'

class RamPageView(TemplateView):
    template_name = 'eightbit/ram.html'

class OutputPageView(TemplateView):
    template_name = 'eightbit/output.html'
