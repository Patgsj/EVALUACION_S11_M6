from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import Book

@login_required
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('add-book')
    return render(request, 'books/add_book.html')

@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'books/list_books.html', {'books': books})

class CustomLoginView(LoginView):
    template_name = 'books/login.html'



# Create your views here.
