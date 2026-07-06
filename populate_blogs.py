import os
import django
import shutil
from django.conf import settings

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import Blog

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


def populate_blogs():
    print('Populating blogs...')
    Blog.objects.all().delete()

    blogs_data = [
        {
            "title": "The Rise of Sustainable Fashion",
            "content": "<p>Sustainable fashion is more than just a trend; it's a movement towards a more conscious and responsible way of living. In this post, we explore the importance of choosing organic fabrics and how they benefit both you and the planet.</p>",
            "image": "blogs/bestseller1.webp",
        },
        {
            "title": "Styling Your Co-ord Sets for Any Occasion",
            "content": "<p>Co-ord sets are the ultimate versatile wardrobe staple. Whether you're dressing for a casual day out or a special evening event, we've got you covered. Discover our top tips for styling your Pindhni co-ord sets.</p>",
            "image": "blogs/bestseller2.webp",
        },
        {
            "title": "Behind the Seams: The Making of a Pindhni Dress",
            "content": "<p>Ever wondered what goes into creating a Pindhni dress? Join us for a behind-the-scenes look at our design process, from the initial sketch to the final stitch. It's a journey of passion, precision, and pure dedication.</p>",
            "image": "blogs/bestseller3.webp",
        },
    ]

    for blog_data in blogs_data:
        # Ensure image is copied from the source folder
        ensure_media_file_from_source(blog_data['image'])
        Blog.objects.create(**blog_data)

    print('Successfully populated blogs.')

if __name__ == '__main__':
    populate_blogs()
