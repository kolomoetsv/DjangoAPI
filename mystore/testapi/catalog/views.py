from django.shortcuts import render
from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from .serializers import BookSerializer
from .models import Book


class BookPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('books_count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('books', data)
        ]))


class BookListAPIView(ListAPIView):

    serializer_class = BookSerializer
    pagination_class = BookPagination
    queryset = Book.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title', 'author', 'genre']


class BookDetailAPIView(RetrieveAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'id'
