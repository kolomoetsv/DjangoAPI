from django.urls import path
from .views import BookListAPIView, BookDetailAPIView

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('books/<str:id>', BookDetailAPIView.as_view(), name='book-detail'),
]
