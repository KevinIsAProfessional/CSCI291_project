# cypher/urls.py
from django.urls import path
from .views import CypherPageView, CaesarPageView, ShaPageView, OtherPageView

urlpatterns = [
    path('cypher/', CypherPageView.as_view(), name='cypher'),
    path('cypher/caesar/', CaesarPageView.as_view(), name='caesar'),
    path('cypher/sha/', ShaPageView.as_view(), name='sha'),
    path('cypher/other/', OtherPageView.as_view(), name='other'),
]
