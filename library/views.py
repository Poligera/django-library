from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'library/base.html')


@login_required
def index(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, 'library/index.html', context)

@login_required
def show(request, id):
    try:
        book = Book.objects.get(pk=id)
        context = {'book': book}
    except Book.DoesNotExist:
        return redirect("https://http.cat/404")
    return render(request, 'library/show.html', context)



