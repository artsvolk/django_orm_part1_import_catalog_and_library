from django.core.management.base import BaseCommand
from django.utils.text import slugify
import csv
from phones.models import Phone

class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                name = row.get('name', 'unknown_phone')
                price = int(row['price'])
                image = row['image']
                release_date = row['release_date']
                lte_exists = row['lte_exists'].lower() == 'true'
                slug = slugify(name)

                phone, created = Phone.objects.update_or_create(
                    id=int(row['id']),
                    defaults={
                        'name': name,
                        'price': price,
                        'image': image,
                        'release_date': release_date,
                        'lte_exists': lte_exists,
                        'slug': slug,
                    }
                )
                if created:
                    self.stdout.write(f"✅ Добавлен телефон: {name}")
                else:
                    self.stdout.write(f"🔄 Обновлён телефон: {name}")