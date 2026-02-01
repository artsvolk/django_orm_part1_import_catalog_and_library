from django.shortcuts import render, get_object_or_404
from .models import Book
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
def book_detail(request, pub_date):
    book = get_object_or_404(Book, pub_date=pub_date)
    dates = list(Book.objects.values_list('pub_date', flat=True).distinct().order_by('pub_date'))
    idx = dates.index(book.pub_date)
    prev_date = dates[idx - 1] if idx > 0 else None
    next_date = dates[idx + 1] if idx < len(dates) - 1 else None
    return render(request, 'books/book_detail.html', {
        'book': book,
        'prev_date': prev_date,
        'next_date': next_date,
    })