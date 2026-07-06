import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import Category

def populate_categories():
    print('Populating categories...')
    Category.objects.all().delete()

    categories_data = [
        "NEW ARRIVALS",
        "DAY WEARS",
        "SUIT",
        "BESTSELLERS",
    ]

    for category_name in categories_data:
        Category.objects.create(name=category_name)

    print('Successfully populated categories.')

if __name__ == '__main__':
    populate_categories()
