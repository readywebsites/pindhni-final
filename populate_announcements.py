import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import Announcement

def populate_announcements():
    print('Populating announcements...')
    Announcement.objects.all().delete()

    announcements_data = [
        {
            "text": "Free Shipping on Orders Above ₹ 200 within Dubai",
            "order": 1,
        },
        {
            "text": "10% off your first online order!",
            "order": 2,
        },
        {
            "text": "New Summer Collection is here!",
            "order": 3,
        },
    ]

    for data in announcements_data:
        Announcement.objects.create(**data)

    print('Successfully populated announcements.')

if __name__ == '__main__':
    populate_announcements()
