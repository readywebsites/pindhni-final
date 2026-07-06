import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import Feature

def populate_features():
    print('Populating features...')
    Feature.objects.all().delete()

    features_data = [
        {
            "icon": "Truck",
            "title": "Free shipping",
            "description": "Free shipping within Dubai on orders above ₹ 200",
            "order": 1,
        },
        {
            "icon": "MessageCircleMore",
            "title": "Customer service",
            "description": "We are available from Monday to Friday to answer your questions.",
            "order": 2,
        },
        {
            "icon": "Shield",
            "title": "Secure payment",
            "description": "Your payment information is processed securely.",
            "order": 3,
        },
        {
            "icon": "Star",
            "title": "Ethical Style",
            "description": "Slow and Sustainable Fashion",
            "order": 4,
        },
    ]

    for feature_data in features_data:
        Feature.objects.create(**feature_data)

    print('Successfully populated features.')

if __name__ == '__main__':
    populate_features()
