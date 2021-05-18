from django.views import View
from django.http import JsonResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from ..models import Book


@method_decorator(csrf_exempt, name='dispatch')
class BookAPIView(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))

        book = Book.objects.create(
            title=data.get('title'),
            author=data.get('author'),
            genre=data.get('genre')
        )

        data = {
            "message": 'New book added to Books with id: {}'.format(book.id)
        }
        return JsonResponse(data, status=201)
