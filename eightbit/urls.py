from django.urls import path 
from .views import EightBitPageView, ClockPageView, RegistersPageView, RamPageView, OutputPageView

urlpatterns = [
        path('eightbit/', EightBitPageView.as_view(), name='eightbit'),
        path('eightbit/clock/', ClockPageView.as_view(), name='clock'),
        path('eightbit/registers/', RegistersPageView.as_view(), name='registers'),
        path('eightbit/ram/', RamPageView.as_view(), name='ram'),
        path('eightbit/output/', OutputPageView.as_view(), name='output'),
        
        ]
