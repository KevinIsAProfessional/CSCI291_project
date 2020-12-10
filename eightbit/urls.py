from django.urls import path 
from .views import EightBitPageView, ClockPageView, RegisterPageView, RamPageView, OutputPageView

urlpatterns = [
        path('eightbit/', EightBitPageView.as_view(), name='eightbit'),
        path('eightbit/clock/', ClockPageView.as_view(), name='clock'),
        path('eightbit/register/', RegisterPageView.as_view(), name='register'),
        path('eightbit/ram/', RamPageView.as_view(), name='ram'),
        path('eightbit/output/', OutputPageView.as_view(), name='output'),
        
        ]
