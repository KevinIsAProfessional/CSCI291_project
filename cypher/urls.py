# cypher/urls.py
from django.urls import path
from .views import CypherPageView, CaesarPageView, ShaPageView, OtherPageView

urlpatterns = [
    path('projects/cypher/', CypherPageView.as_view(), name='cypher'),
    path('projects/cypher/caesar/', CaesarPageView.as_view(), name='caesar'),
    path('projects/cypher/sha/', ShaPageView.as_view(), name='sha'),
    path('projects/cypher/other/', OtherPageView.as_view(), name='other'),
]
