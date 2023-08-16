from django.shortcuts import render
from books.models import Book


class BookExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Book.DoesNotExist):
            return render(request, 'error.html', {'message': 'Book not found!'})
