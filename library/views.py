from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Book
from django.shortcuts import get_object_or_404
# from django import defaults

# books = [
#     { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
#     { 'id': 2, 'title': 'The Meaning of Life', 'author': 'Douglas Adams'},
#     { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
# ]titel=""
# Create your views here.
def home(request):
    # context = [book['title'] for book in books]
    book = ""
    books = Book.objects.all()
    for i in books:
        book += f"<li>\"{i.title}\" by {i.author}</li>"
    return HttpResponse(f"<ol><h2>{book}</h2></ol>")

def show(request, id):
    # context = books[id-1] if id <= len(books) else None
    # book = get_object_or_404(Book, pk=id)
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return redirect("https://http.cat/404")
    # if id <= len(books) and id > 0:
    #     book = books[id -1]
    #     return HttpResponse(f"Book: <h3>{book['title']} by {book['author']}</h3>")
    return HttpResponse(f"Book: <h3>{book}</h3>")
    # else:
    #     redirect("https://http.cat/404")
