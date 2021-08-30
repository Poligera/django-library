from django.shortcuts import render, redirect
from .models import Book


def home(request):
    return render(request, 'library/base.html')


def index(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, 'library/index.html', context)

def show(request, id):
    try:
        book = Book.objects.get(pk=id)
        context = {'book': book}
    except Book.DoesNotExist:
        return redirect("https://http.cat/404")
    return render(request, 'library/show.html', context)



