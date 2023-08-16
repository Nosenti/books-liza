from django.shortcuts import render
from .models import Book


def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/list.html', {'books': books})


def books_list(request):
    query = request.GET.get('search', '')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'books/list.html', {'books': books})
