from django.urls import path
from .views import *

url_patterns = [
    path('librarys/', LibraryListAPIView.as_view()),
    path('upload/', BookUploadView.as_view()),
    path('book/<int:pk>/', BookRetrieveUpdateDeleteView.as_view())
]