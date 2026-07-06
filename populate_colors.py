import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import Color

def populate_colors():
    print('Populating colors...')
    Color.objects.all().delete()

    colors_data = [
        {"name": "Lavender", "hex": "#E6E6FA"},
        {"name": "Sage Green", "hex": "#87A96B"},
        {"name": "Coral", "hex": "#FF7F50"},
        {"name": "Mustard Yellow", "hex": "#E1AD01"},
        {"name": "Dusty Rose", "hex": "#DCAE96"},
        {"name": "Indigo Blue", "hex": "#4B0082"},
        {"name": "Crimson Red", "hex": "#DC143C"},
        {"name": "Teal", "hex": "#008080"},
        {"name": "Rust", "hex": "#B7410E"},
        {"name": "Peach", "hex": "#FFDAB9"},
        {"name": "Olive Green", "hex": "#808000"},
        {"name": "Charcoal Black", "hex": "#36454F"},
        {"name": "Off-White", "hex": "#F5F5F0"},
    ]

    for color in colors_data:
        Color.objects.create(name=color["name"], hex=color["hex"])

    print('Successfully populated colors.')

if __name__ == '__main__':
    populate_colors()
