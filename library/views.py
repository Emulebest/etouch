from rest_framework import generics, status
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework import mixins
from .serializers import *


class BookUploadView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (FileUploadParser,)

    def post(self, request, filename):
        book = Book.objects.create(book_path=f"books/{request.user.username}/{filename}", name=filename, current_page=0,
                                   status=StatusChoices.OPEN)
        library = Library.objects.get(user=request.user)
        library.books.add(book)
        library.save()
        file_obj = request.data["file"]
        with open(f"books/{request.user.username}/{filename}", "w+") as file:
            file.write(file_obj)
        return Response({"result": "ok"}, status=status.HTTP_202_ACCEPTED)


class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)


class LibraryListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LibrarySerializer

    def get_queryset(self):
        return Library.objects.get(user=self.request.user)
