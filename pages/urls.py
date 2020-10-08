# pages/urls.py
from django.urls import path

from .views import HomePageView, ConstructionPageView

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('construction/', ConstructionPageView.as_view(), name='construction')
        ]
