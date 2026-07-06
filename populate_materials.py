import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import Material

def populate_materials():
    print('Populating materials...')
    Material.objects.all().delete()

    materials_data = [
        "Cotton",
        "Silk",
        "Georgette",
        "Chiffon",
        "Crepe",
        "Velvet",
        "Organza",
        "Banarasi Silk",
        "Chanderi",
        "Rayon",
        "Linen",
        "Satin",
        "Muslin",
        "Net"
    ]

    for mat_name in materials_data:
        Material.objects.create(name=mat_name)

    print('Successfully populated materials.')

if __name__ == '__main__':
    populate_materials()
