from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import *


class DeviceListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return Device.objects.get(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)