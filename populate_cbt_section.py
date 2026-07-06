import os
import django
from PIL import Image
from django.conf import settings

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import ComfortBeyondTimeSection

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
        img = Image.new('RGB', (1024, 1024), color=(128, 128, 128))
        img.save(full_path, 'WEBP')
        print(f"Created placeholder image at: {full_path}")
    except Exception as e:
        print(f"Error creating placeholder image {full_path}: {e}")


def populate_cbt_section():
    print('Populating Comfort Beyond Time section...')
    ComfortBeyondTimeSection.objects.all().delete()

    data = {
        "title": "Comfort Beyond Time",
        "subtitle": "EXPERIENCE THE LUXURY OF ORGANIC FABRICS",
        "description": """
        <p>At Pindhni, we believe in the art of mindful living, and that begins with the clothes you wear. Our collections are crafted from the finest organic fabrics, offering a touch of nature's luxury against your skin. Each piece is a testament to our commitment to sustainability, quality, and timeless style.</p>
        <p>Embrace a wardrobe that not only looks beautiful but feels incredible, knowing that every thread is woven with respect for the planet and for you.</p>
        """,
        "image1": "cbt_section/cord1.webp",
        "image2": "cbt_section/banner1.webp",
    }

    # Ensure placeholder images exist before creating the object
    ensure_placeholder_image(data['image1'])
    ensure_placeholder_image(data['image2'])

    ComfortBeyondTimeSection.objects.create(**data)

    print('Successfully populated Comfort Beyond Time section.')

if __name__ == '__main__':
    populate_cbt_section()