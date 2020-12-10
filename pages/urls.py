# pages/urls.py
from django.urls import path

from .views import HomePageView, ConstructionPageView, ProjectsPageView, BlogPageView, PhotoPageView, ContactPageView

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('construction/', ConstructionPageView.as_view(), name='construction'),
        # projects section
        path('projects/', ProjectsPageView.as_view(), name='projects'),
        # blog section
        path('blog/', BlogPageView.as_view(), name='blog'),
        # photo section
        path('photos/', PhotoPageView.as_view(), name='photos'),
        # contact
        path('contact/', ContactPageView.as_view(), name='contact')
        ]
