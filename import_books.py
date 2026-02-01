import os
import django
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()
from books.models import Book
books_data = [
    {"title": "Война и мир", "author": "Л.Н. Толстой", "pub_date": "1869-01-01"},
    {"title": "1984", "author": "Джордж Оруэл", "pub_date": "1949-06-08"},
    {"title": "Скотный двор", "author": "Джордж Оруэл", "pub_date": "1945-08-17"},
    {"title": "В память о прошлом земли", "author": "Лю Цысинь", "pub_date": "2006-01-01"},
]
for data in books_data:
    book = Book(**data)
    book.save()
    print(f"✅ {book.title}")