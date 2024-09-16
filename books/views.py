from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    template_name = "book_list.html"
    model = Book
