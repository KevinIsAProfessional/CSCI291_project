# cypher/urls.py
from django.urls import path
from .views import CypherPageView, CaesarPageView, ShaPageView, OtherPageView

urlpatterns = [
    path('cypher/', CypherPageView.as_view(), name='cypher'),
    path('caesar/', CaesarPageView.as_view(), name='caesar'),
    path('sha/', ShaPageView.as_view(), name='sha'),
    path('other/', OtherPageView.as_view, name='other'),
]
