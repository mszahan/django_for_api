from django.db.models.query import QuerySet
from rest_framework import generics, serializers
from books.models import Book
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
