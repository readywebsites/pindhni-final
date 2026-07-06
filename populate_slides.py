import os
import django
from PIL import Image
from django.conf import settings

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import HeroSlide

def ensure_placeholder_image(image_path):
    """
    Ensures a placeholder image exists at the given path relative to MEDIA_ROOT.
    If not, it creates a simple placeholder image.
    """
    if not image_path:
        return

    full_path = os.path.join(settings.MEDIA_ROOT, image_path)

    if os.path.exists(full_path):
        return

    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    try:
        # Use different dimensions for mobile images if needed
        if 'mobile' in image_path:
            width, height = 576, 1024
        else:
            width, height = 1920, 1080
        
        img = Image.new('RGB', (width, height), color=(128, 128, 128))
        img.save(full_path, 'WEBP')
        print(f"Created placeholder image at: {full_path}")
    except Exception as e:
        print(f"Error creating placeholder image {full_path}: {e}")


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
        # Ensure placeholder images exist before creating the object
        ensure_placeholder_image(slide_data.get('image'))
        ensure_placeholder_image(slide_data.get('mobile_image'))
        HeroSlide.objects.create(**slide_data)

    print('Successfully populated hero slides.')

if __name__ == '__main__':
    populate_slides()