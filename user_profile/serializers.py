from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        fields = ('name', 'surname')
        read_only = ('id', 'user')
