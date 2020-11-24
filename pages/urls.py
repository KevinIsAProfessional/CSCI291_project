# pages/urls.py
from django.urls import path

from .views import HomePageView, ConstructionPageView, PhotoPageView

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('construction/', ConstructionPageView.as_view(), name='construction'),
        path('photos/', PhotoPageView.as_view(), name='photos'),
        ]
