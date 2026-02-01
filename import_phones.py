import os
import django
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()
from phones.models import Phone
with open('phones.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        name = row.get('name', 'unknown_phone')
        slug = name.lower().replace(' ', '-').replace('"', '').replace('/', '').replace('(', '').replace(')', '')
        if not slug or slug == '-':
            slug = f'phone-{row["id"]}'
        image = row['image'].replace('phones/', '').strip()
        phone = Phone(
            id=int(row['id']),
            name=name,
            price=int(row['price']),
            image=image,
            release_date=row['release_date'],
            lte_exists=row['lte_exists'].lower() == 'true',
            slug=slug
        )
        phone.save()
        print(f"✅ Добавлен телефон: {name}")