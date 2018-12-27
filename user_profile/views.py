from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from etouch.settings import SITE_ROOT
from .serializers import *
import os
from library.models import Library


class ListProfilesAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.get(user=self.request.user)

    def perform_create(self, serializer):
        os.mkdir(f"{SITE_ROOT}/{self.request.user.username}")
        Library.objects.create(user=self.request.user)
        serializer.save(user=self.request.user)
