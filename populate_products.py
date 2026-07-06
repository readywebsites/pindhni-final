import os
import django
import re

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

import random
from api.models import Product, Category, Size, Color, Material, ProductSize

def populate_products():
    print('Populating products...')
    Product.objects.all().delete()

    products_data = [
        {
            "image": "products/newarrival1.webp",
            "name": "Beige Cotton Linen Co-ord Set with Vertical Stripe Print & Flowing Relaxed Silhouette | Virelle",
            "price": "₹245.00",
            "categories": ["NEW ARRIVALS"],
        },
        {
            "image": "products/newarrival2.webp",
            "name": "Cotton Striped Co-ord Set with Button-Down Shirt & Straight-Leg Trousers | Nyra",
            "price": "₹185.00",
            "categories": ["NEW ARRIVALS"],
        },
        {
            "image": "products/newarrival3.webp",
            "name": "Cotton Striped Co-ord Set with Long Sleeve Top, Waist Tie Detail & Straight-Leg Trousers | Selis",
            "price": "₹185.00",
            "categories": ["NEW ARRIVALS"],
        },
        {
            "image": "products/newarrival4.webp",
            "name": "Cotton Co-ord Set with Relaxed-Fit Top, Matching Pants & Side Pockets | Pure Cotton Co-ord Set",
            "price": "₹162.50",
            "categories": ["NEW ARRIVALS"],
        },
        {
            "image": "products/cord1.webp",
            "name": "Cotton Floral Print Maxi Dress with V-Neck, Long Sleeves & Gathered Bodice | Aveline",
            "price": "₹259.09",
            "categories": ["DAY WEARS"],
        },
        {
            "image": "products/cord2.webp",
            "name": "Cotton Botanical Print Maxi Dress with V-Neck, Long Sleeves & Gathered Bodice | Solira",
            "price": "₹259.09",
            "categories": ["DAY WEARS"],
        },
        {
            "image": "products/cord3.webp",
            "name": "Cotton Floral Print Maxi Dress with V-Neck, Long Sleeves & Gathered Bodice | Virelle",
            "price": "₹259.09",
            "categories": ["DAY WEARS", "BESTSELLERS"],
        },
        {
            "image": "products/cord4.webp",
            "name": "Cotton Botanical Print Maxi Dress with V-Neck, Long Sleeves & Gathered Bodice | Arlena",
            "price": "₹259.09",
            "categories": ["DAY WEARS"],
        },
        {
            "image": "products/suit1.webp",
            "name": "Pindhni Best Material Kurtis",
            "price": "₹100.00",
            "categories": ["SUIT"],
        },
        {
            "image": "products/suit2.webp",
            "name": "Pindhni Best Material Kurtis",
            "price": "₹100.00",
            "categories": ["SUIT"],
        },
        {
            "image": "products/suit3.webp",
            "name": "Pindhni Best Material Kurtis",
            "price": "₹100.00",
            "categories": ["SUIT", "BESTSELLERS"],
        },
        {
            "image": "products/suit4.webp",
            "name": "Pindhni Best Material Kurtis",
            "price": "₹100.00",
            "categories": ["SUIT"],
        },
        {
            "image": "products/bestseller1.webp",
            "name": "Pindhni Best Material Bestsellers",
            "price": "₹100.00",
            "categories": ["BESTSELLERS"],
        },
        {
            "image": "products/bestseller2.webp",
            "name": "Pindhni Best Material Bestsellers",
            "price": "₹100.00",
            "categories": ["BESTSELLERS"],
        },
        {
            "image": "products/bestseller3.webp",
            "name": "Pindhni Best Material Bestsellers",
            "price": "₹100.00",
            "categories": ["BESTSELLERS"],
        },
        {
            "image": "products/bestseller4.webp",
            "name": "Pindhni Best Material Bestsellers",
            "price": "₹100.00",
            "categories": ["BESTSELLERS"],
        },
    ]

    # Fetch existing/pre-populate Size, Color, Material
    sizes_db = list(Size.objects.all())
    if not sizes_db:
        print("Sizes table is empty, pre-populating sizes...")
        sizes_data = ['XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL', '4XL']
        for sz_name in sizes_data:
            Size.objects.get_or_create(name=sz_name)
        sizes_db = list(Size.objects.all())

    colors_db = list(Color.objects.all())
    if not colors_db:
        print("Colors table is empty, pre-populating colors...")
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
        for col_info in colors_data:
            Color.objects.get_or_create(name=col_info["name"], hex=col_info["hex"])
        colors_db = list(Color.objects.all())

    materials_db = list(Material.objects.all())
    if not materials_db:
        print("Materials table is empty, pre-populating materials...")
        materials_data = [
            "Cotton", "Silk", "Georgette", "Chiffon", "Crepe", "Velvet",
            "Organza", "Banarasi Silk", "Chanderi", "Rayon", "Linen", "Satin",
            "Muslin", "Net"
        ]
        for mat_name in materials_data:
            Material.objects.get_or_create(name=mat_name)
        materials_db = list(Material.objects.all())

    for product_data in products_data:
        price_str = product_data['price']
        # Remove currency symbol and commas
        price_cleaned = re.sub(r'[^\d.]', '', price_str)
        try:
            price = float(price_cleaned)
        except ValueError:
            print(f"Could not parse price for {product_data['name']}: {price_str}")
            continue

        category_names = product_data.get('categories', [])
        is_new_arr = "NEW ARRIVALS" in [c.upper() for c in category_names]
        is_best = "BESTSELLERS" in [c.upper() for c in category_names]

        # Available detail images to sample from
        all_avail_images = [
            "products/newarrival1.webp", "products/newarrival2.webp",
            "products/newarrival3.webp", "products/newarrival4.webp",
            "products/cord1.webp", "products/cord2.webp",
            "products/cord3.webp", "products/cord4.webp",
            "products/suit1.webp", "products/suit2.webp",
            "products/suit3.webp", "products/suit4.webp",
            "products/bestseller1.webp", "products/bestseller2.webp",
            "products/bestseller3.webp", "products/bestseller4.webp",
        ]
        # Exclude current image from the pool to avoid duplicate detail images
        pool = [img for img in all_avail_images if img != product_data['image']]
        sampled = random.sample(pool, k=3)
        # Determine discount randomly
        discount_choice = random.random()
        if discount_choice < 0.3:
            discount_type = 'percent'
            discount_value = random.choice([10.00, 15.00, 20.00, 25.00, 30.00])
        elif discount_choice < 0.5:
            discount_type = 'amount'
            discount_value = random.choice([30.00, 40.00, 50.00, 60.00])
        else:
            discount_type = 'none'
            discount_value = 0.00

        product = Product.objects.create(
            name=product_data['name'],
            price=price,
            image=product_data['image'],
            description=f"Description for {product_data['name']}",
            in_stock=(random.random() > 0.15),
            is_new_arrival=is_new_arr,
            is_bestseller=is_best,
            is_featured=(random.random() > 0.7),
            detail_image_1=sampled[0],
            detail_image_2=sampled[1],
            detail_image_3=sampled[2],
            details="<p>• Exquisite bespoke design with high-density weave construction.</p><p>• Relaxed designer fit tailored for all silhouettes.</p><p>• Double stitched seams with premium embroidery details.</p>",
            material_care="<p>• Fabric: Premium blend of fine fibers.</p><p>• Gentle hand wash in cold water or professional dry clean.</p><p>• Do not bleach. Cool iron on reverse side.</p>",
            shipping="<p>• Dispatched within 24-48 hours from our fulfillment hub.</p><p>• Free shipping across India. International rates calculated at checkout.</p><p>• 7-day hassle-free return and exchange window.</p>",
            discount_type=discount_type,
            discount_value=discount_value,
        )
        
        for cat_name in category_names:
            category, _ = Category.objects.get_or_create(name=cat_name)
            product.categories.add(category)

        # Match Material from title
        matched_materials = []
        for mat in materials_db:
            if re.search(r'\b' + re.escape(mat.name) + r'\b', product_data['name'], re.IGNORECASE):
                matched_materials.append(mat)
        
        # If no material matched from title, assign 1-2 random materials
        if not matched_materials and materials_db:
            matched_materials = random.sample(materials_db, k=random.randint(1, min(2, len(materials_db))))
            
        for mat in matched_materials:
            product.materials.add(mat)

        # Match Color from title
        matched_colors = []
        for col in colors_db:
            if re.search(r'\b' + re.escape(col.name) + r'\b', product_data['name'], re.IGNORECASE):
                matched_colors.append(col)
            elif col.name == "Off-White" and re.search(r'\bBeige\b', product_data['name'], re.IGNORECASE):
                matched_colors.append(col)

        # If no color matched from title, assign 1-2 random colors
        if not matched_colors and colors_db:
            matched_colors = random.sample(colors_db, k=random.randint(1, min(2, len(colors_db))))

        for col in matched_colors:
            product.colors.add(col)

        # Match Size from title (rare but checked)
        matched_sizes = []
        for sz in sizes_db:
            if re.search(r'\b' + re.escape(sz.name) + r'\b', product_data['name']):
                matched_sizes.append(sz)
                
        # If no size matched from title, assign 3-5 random sizes
        if not matched_sizes and sizes_db:
            matched_sizes = random.sample(sizes_db, k=random.randint(3, min(5, len(sizes_db))))

        for sz in matched_sizes:
            ProductSize.objects.create(
                product=product,
                size=sz,
                in_stock=(random.random() > 0.15)
            )

    print('Successfully populated products.')

if __name__ == '__main__':
    populate_products()
