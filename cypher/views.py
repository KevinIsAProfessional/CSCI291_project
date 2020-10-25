from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import InputForm

class CypherPageView(TemplateView):
    template_name = 'cypher/cypher.html'

class CaesarPageView(TemplateView):
    template_name = 'cypher/caesar.html'

    def input_view(request):
        context={}
        context['form']=InputForm()
        return render(request, 'cypher/cypher.html', context)

class ShaPageView(TemplateView):
    template_name = 'cypher/sha.html'

class OtherPageView(TemplateView):
    template_name = 'cypher/other.html'
