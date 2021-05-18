from django.views import View
from django.http import JsonResponse
from django.core import serializers
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from ..models import Book


@method_decorator(csrf_exempt, name='dispatch')
class BookAPIView(View):
    def post(self, request):
        # Decode and parse the incoming request's body into an object we can work with
        data = json.loads(request.body.decode("utf-8"))

        # Persist a Book to our database, via the create() method of the Model class,
        # filling it with our extracted data.
        book = Book.objects.create(
            title=data.get('title'),
            author=data.get('author'),
            genre=data.get('genre')
        )

        data = {
            "message": 'New book added to Books with id: {}'.format(book.id)
        }
        # Convert Python dictionary to a valid JSON object that is sent over HTTP back to the client.
        # Set the status code to 201 to signify resource creation on the server-end.
        return JsonResponse(data, status=201)

    def get(self, request):
        books_data = serializers.serialize("json", Book.objects.all())
        books_count = Book.objects.count()

        data = {
            'items': books_data,
            'count': books_count,
        }

        return JsonResponse(data, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class BookAPIUpdateView(View):
    def patch(self, request, book_id):
        data = json.loads(request.body.decode("utf-8"))
        book = Book.objects.get(id=book_id)
        book.author = data['author']
        book.save()

        new_record = Book.objects.filter(id=book_id)
        body = serializers.serialize('json', new_record)

        data = {
            'book': body,
            'message': 'Book {} has been updated'.format(book_id)
        }

        return JsonResponse(data)

    def delete(self, request, book_id):
        book = Book.objects.get(id=book_id)
        book.delete()

        data = {
            'message': 'Book {} has been deleted'.format(book.id)
        }

        return JsonResponse(data)
