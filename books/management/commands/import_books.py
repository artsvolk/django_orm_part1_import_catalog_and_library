from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Import books'

    def handle(self, *args, **options):
        books_data = [
            {"title": "Война и мир", "author": "Л.Н. Толстой", "pub_date": "1869-01-01"},
            {"title": "1984", "author": "Джордж Оруэл", "pub_date": "1949-06-08"},
            {"title": "Скотный двор", "author": "Джордж Оруэл", "pub_date": "1945-08-17"},
            {"title": "В память о прошлом земли", "author": "Лю Цысинь", "pub_date": "2006-01-01"},
        ]

        for data in books_data:
            book, created = Book.objects.update_or_create(
                title=data['title'],
                author=data['author'],
                pub_date=data['pub_date'],
                defaults=data
            )
            if created:
                self.stdout.write(f"✅ Добавлена книга: {data['title']}")
            else:
                self.stdout.write(f"🔄 Обновлена книга: {data['title']}")