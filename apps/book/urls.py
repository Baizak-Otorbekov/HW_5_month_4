from django.urls import path
from apps.book.views import BookListView, BookCreateView, BookUpdateView,\
BookDetailView, BookDeleteView

urlpatterns = [
    path("", BookListView.as_view(), name='book-list'),
    path("create", BookCreateView.as_view(), name='create'),
    path("<int:pk>/update/", BookUpdateView.as_view(), name='update-book'),
    path("<int:pk>/", BookDetailView.as_view(), name='detail-book'),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name='delete')
]