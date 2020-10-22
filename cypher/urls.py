# cypher/urls.py
from django.urls import path
from .views import CypherPageView, CaesarPageView

urlpatterns = [
    path('cypher/', CypherPageView.as_view(), name='cypher'),
    path('caesar/', CaesarPageView.as_view(), name='caesar')
]
