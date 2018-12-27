from rest_framework import serializers
from .models import *


class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = ('name', 'status')
        read_only = ('id', 'current_page')
        extra_kwargs = {'status': {'required': False}}


class LibrarySerializer(serializers.Serializer):
    books = BookSerializer(read_only=True, many=True)

    class Meta:
        model = Library
        read_only = ('books', 'user', 'id')
