from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter

from .serializers import BookSerializer
from .models import Book


class BookListAPIView(ListAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title', 'author', 'genre']


class BookDetailAPIView(RetrieveAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'id'
