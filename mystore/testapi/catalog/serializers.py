from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    author = serializers.CharField(required=True)
    genre = serializers.CharField(required=True)

    class Meta:
        model = Book
        fields = '__all__'
