import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import Blog

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
        Blog.objects.create(**blog_data)

    print('Successfully populated blogs.')

if __name__ == '__main__':
    populate_blogs()
