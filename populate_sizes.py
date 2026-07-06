import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import Size

def populate_sizes():
    print('Populating sizes...')
    Size.objects.all().delete()

    sizes_data = ['XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL', '4XL']
    for size_name in sizes_data:
        Size.objects.create(name=size_name)

    print('Successfully populated sizes.')

if __name__ == '__main__':
    populate_sizes()
