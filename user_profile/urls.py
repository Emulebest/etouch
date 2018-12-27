from django.urls import path
from .views import *

url_patterns = [
    path('profiles/', ListProfilesAPIView.as_view()),
]