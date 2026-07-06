import os
import django
import shutil
from django.conf import settings

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import ComfortBeyondTimeSection

def ensure_media_file_from_source(image_path_fragment):
    """
    Ensures an image exists at the given path in the media directory,
    copying it from the source directory ('dist/images') if it doesn't exist.
    """
    if not image_path_fragment:
        return

    destination_path = os.path.join(settings.MEDIA_ROOT, image_path_fragment)
    image_filename = os.path.basename(image_path_fragment)
    source_path = os.path.join(settings.BASE_DIR, 'dist', 'images', image_filename)

    if os.path.exists(destination_path):
        return

    if not os.path.exists(source_path):
        print(f"Warning: Source image not found at '{source_path}'. Cannot copy.")
        return

    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    try:
        shutil.copy2(source_path, destination_path)
        print(f"Copied '{source_path}' to '{destination_path}'")
    except Exception as e:
        print(f"Error copying file: {e}")


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

    # Ensure images are copied from the source folder
    ensure_media_file_from_source(data['image1'])
    ensure_media_file_from_source(data['image2'])

    ComfortBeyondTimeSection.objects.create(**data)

    print('Successfully populated Comfort Beyond Time section.')

if __name__ == '__main__':
    populate_cbt_section()
