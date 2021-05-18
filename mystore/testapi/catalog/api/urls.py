from django.urls import path
from . import api_views

urlpatterns = [
    path('books/', api_views.BookAPIView.as_view()),
    path('update-book/<int:book_id>', api_views.BookAPIUpdateView.as_view()),
]
