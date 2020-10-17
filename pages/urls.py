# pages/urls.py
from django.urls import path

from .views import HomePageView, ConstructionPageView, CypherPageView

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('construction/', ConstructionPageView.as_view(), name='construction'),
        path('cypher/', CypherPageView.as_view(), name='cypher')
        ]
