# pages/views.py

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class ConstructionPageView(TemplateView):
    template_name = 'construction.html'

class ProjectsPageView(TemplateView):
    template_name = 'base_projects.html'

class BlogPageView(TemplateView):
    template_name = 'construction.html'

class PhotoPageView(TemplateView):
    template_name = 'photos.html'
    
class ContactPageView(TemplateView):
    template_name = 'construction.html'
