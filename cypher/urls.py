# cypher/urls.py
from django.urls import path
from .views import CypherPageView

urlpatterns = [
    path('cypher/', CypherPageView.as_view(), name='cypher'),
]
