import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import ComfortBeyondTimeSection

def populate_cbt_section():
    print('Populating Comfort Beyond Time section...')
    ComfortBeyondTimeSection.objects.all().delete()

    ComfortBeyondTimeSection.objects.create(
        title="Comfort Beyond Time",
        subtitle="EXPERIENCE THE LUXURY OF ORGANIC FABRICS",
        description="""
        <p>At Pindhni, we believe in the art of mindful living, and that begins with the clothes you wear. Our collections are crafted from the finest organic fabrics, offering a touch of nature's luxury against your skin. Each piece is a testament to our commitment to sustainability, quality, and timeless style.</p>
        <p>Embrace a wardrobe that not only looks beautiful but feels incredible, knowing that every thread is woven with respect for the planet and for you.</p>
        """,
        image1="cbt_section/cord1.webp",
        image2="cbt_section/banner1.webp",
    )

    print('Successfully populated Comfort Beyond Time section.')

if __name__ == '__main__':
    populate_cbt_section()
