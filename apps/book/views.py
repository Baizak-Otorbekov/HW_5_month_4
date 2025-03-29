from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,\
UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.book.forms import BookForm
from apps.book.models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book-list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(is_active=True).order_by('-created')

class BookCreateView(CreateView):
    model = Book
    template_name = 'book-create.html'
    form_class = BookForm
    success_url = reverse_lazy("book-list")

class BookDetailView(DetailView):
    model = Book
    template_name = 'book-detail.html'
    context_object_name = 'books'

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book-create.html'
    form_class = BookForm
    success_url = reverse_lazy("book-list")

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'delete.html'
    context_object_name = 'book'
    success_url = reverse_lazy('book-list')