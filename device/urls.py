from django.urls import path
from .views import *

url_patterns = [
    path('devices/', DeviceListAPIView.as_view()),
]