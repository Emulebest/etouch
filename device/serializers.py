from rest_framework import serializers
from .models import *


class DeviceSerializer(serializers.Serializer):
    class Meta:
        model = Device
        fields = ('name', 'address')
        read_only = ('user', 'id')
