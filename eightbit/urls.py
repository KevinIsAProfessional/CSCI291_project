from django.urls import path 
from .views import EightBitPageView, ClockPageView, RegistersPageView, RamPageView, OutputPageView

urlpatterns = [
        path('projects/eightbit/', EightBitPageView.as_view(), name='eightbit'),
        path('projects/eightbit/clock/', ClockPageView.as_view(), name='clock'),
        path('projects/eightbit/registers/', RegistersPageView.as_view(), name='registers'),
        path('projects/eightbit/ram/', RamPageView.as_view(), name='ram'),
        path('projects/eightbit/output/', OutputPageView.as_view(), name='output'),

        
        ]
