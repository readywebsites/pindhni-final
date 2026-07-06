import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import Store

def populate_stores():
    print('Populating stores...')
    Store.objects.all().delete()

    stores_data = [
        {
            "title": "Pindhni Flagship Store",
            "address": "123 Fashion Avenue\nMetropolis\n10001",
            "address_link": "https://www.google.com/maps",
            "link_text": "Find Us",
        },
        {
            "title": "The Organic Boutique",
            "address": "456 Green Way\nEcotown\n20002",
            "address_link": "https://www.google.com/maps",
            "link_text": "Get Directions",
        },
        {
            "title": "Downtown Style Hub",
            "address": "789 Central Plaza\nDowntown\n30003",
            "address_link": "https://www.google.com/maps",
        },
    ]

    for store_data in stores_data:
        Store.objects.create(**store_data)

    print('Successfully populated stores.')

if __name__ == '__main__':
    populate_stores()
