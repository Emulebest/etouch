from enum import Enum

from django.contrib.auth.models import User
from django.db import models


class StatusChoices(Enum):
    OPEN = "open"
    ARCHIVED = "archived"


class Book(models.Model):
    book_path = models.FilePathField()
    name = models.TextField()
    current_page = models.IntegerField()
    status = models.TextField(choices=[(tag, tag.value) for tag in StatusChoices])


class Library(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name="lib")
