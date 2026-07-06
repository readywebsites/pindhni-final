import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import HeroSlide

def populate_slides():
    print('Populating hero slides...')
    HeroSlide.objects.all().delete()

    slides_data = [
        {
            "image": "hero_slides/banner1.webp",
            "mobile_image": "hero_slides/mobile/phone-banner1.webp",
            "button_text": "Shop Now",
            "button_link": "/collections/all",
            "button_alignment": "center",
            "order": 1,
        },
        {
            "image": "hero_slides/banner2.webp",
            "mobile_image": "hero_slides/mobile/phone-banner2.webp",
            "button_text": "Discover More",
            "button_link": "/pages/about-us",
            "button_alignment": "left",
            "order": 2,
        },
        {
            "image": "hero_slides/banner3.webp",
            "mobile_image": "hero_slides/mobile/phone-banner3.webp",
            "button_text": "View Collection",
            "button_link": "/collections/new-arrivals",
            "button_alignment": "right",
            "order": 3,
            "secondary_button_text": "Learn More",
            "secondary_button_link": "/pages/story",
        },
        {
            "image": "hero_slides/banner4.webp",
            "mobile_image": "hero_slides/mobile/phone-banner4.webp",
            "button_text": "Shop Sale",
            "button_link": "/collections/sale",
            "button_alignment": "center",
            "order": 4,
        },
        {
            "image": "hero_slides/banner5.webp",
            "mobile_image": "hero_slides/mobile/phone-banner5.webp",
            "button_text": "Contact Us",
            "button_link": "/pages/contact",
            "button_alignment": "center",
            "order": 5,
        },
    ]

    for slide_data in slides_data:
        HeroSlide.objects.create(**slide_data)

    print('Successfully populated hero slides.')

if __name__ == '__main__':
    populate_slides()
