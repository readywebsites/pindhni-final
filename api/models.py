from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    show_on_navbar = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)
    hex = models.CharField(max_length=7, default='#000000')

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', default='')
    categories = models.ManyToManyField('Category', related_name='products')
    sizes = models.ManyToManyField('Size', through='ProductSize', related_name='products', blank=True)
    colors = models.ManyToManyField('Color', related_name='products', blank=True)
    materials = models.ManyToManyField('Material', related_name='products', blank=True)
    in_stock = models.BooleanField(default=True)
    is_new_arrival = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    detail_image_1 = models.ImageField(upload_to='products/details/', blank=True, null=True)
    detail_image_2 = models.ImageField(upload_to='products/details/', blank=True, null=True)
    detail_image_3 = models.ImageField(upload_to='products/details/', blank=True, null=True)
    detail_image_4 = models.ImageField(upload_to='products/details/', blank=True, null=True)
    detail_image_5 = models.ImageField(upload_to='products/details/', blank=True, null=True)
    detail_image_6 = models.ImageField(upload_to='products/details/', blank=True, null=True)
    detail_image_7 = models.ImageField(upload_to='products/details/', blank=True, null=True)
    detail_image_8 = models.ImageField(upload_to='products/details/', blank=True, null=True)
    detail_image_9 = models.ImageField(upload_to='products/details/', blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    material_care = models.TextField(blank=True, null=True)
    shipping = models.TextField(blank=True, null=True)
    discount_type = models.CharField(
        max_length=10,
        default='none',
        choices=[('none', 'None'), ('percent', 'Percentage'), ('amount', 'Amount')]
    )
    discount_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_sizes')
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)

    class Meta:
        unique_together = ('product', 'size')

    def __str__(self):
        return f"{self.product.name} - {self.size.name} ({'In Stock' if self.in_stock else 'Out of Stock'})"

class HeroSlide(models.Model):
    image = models.ImageField(upload_to='hero_slides/') # Desktop image
    mobile_image = models.ImageField(upload_to='hero_slides/mobile/', blank=True, null=True) # Mobile image
    button_text = models.CharField(max_length=50)
    button_link = models.CharField(max_length=200, default='#')
    button_alignment = models.CharField(max_length=10, default='center', choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])
    secondary_button_text = models.CharField(max_length=50, blank=True, null=True)
    secondary_button_link = models.CharField(max_length=200, blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Order of the slide in the slider.")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Slide {self.order}"

class ComfortBeyondTimeSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.ImageField(upload_to='cbt_section/') # Vertical
    image2 = models.ImageField(upload_to='cbt_section/') # Horizontal

    class Meta:
        verbose_name = "Comfort Beyond Time Section"
        verbose_name_plural = "Comfort Beyond Time Sections"

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class BlogCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "blog categories"

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    published_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.excerpt:
            self.excerpt = ' '.join(self.content.split()[:20]) + '...'
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

class Store(models.Model):
    title = models.CharField(max_length=100)
    address = models.TextField()
    address_link = models.URLField(max_length=500)
    link_text = models.CharField(max_length=100, default="View on Map")

    def __str__(self):
        return self.title

class Feature(models.Model):
    ICON_CHOICES = [
        ('Truck', 'Truck'),
        ('MessageCircleMore', 'Customer Service'),
        ('Shield', 'Secure Payment'),
        ('Star', 'Ethical Style'),
    ]
    
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

# Footer Models
class FooterSection(models.Model):
    newsletter_text = models.TextField()
    copyright_line_1 = models.CharField(max_length=200)
    copyright_line_2 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "Footer Content"

class SocialLink(models.Model):
    ICON_CHOICES = [
        ('Camera', 'Camera'),
        ('Music', 'Music'),
        ('MessageCircle', 'Message Circle'),
    ]
    footer_section = models.ForeignKey(FooterSection, related_name='social_links', on_delete=models.CASCADE)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    link = models.URLField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.get_icon_display()

class FooterMenu(models.Model):
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class FooterMenuItem(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    menu = models.ForeignKey(FooterMenu, related_name='items', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Announcement(models.Model):
    text = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text

class Policy(models.Model):
    title = models.CharField(max_length=255)
    policy = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "policies"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
        try:
            menu = FooterMenu.objects.filter(title__iexact="Our Policies").first()
            if menu:
                link_path = f"/{self.slug}"
                item_exists = FooterMenuItem.objects.filter(menu=menu, link=link_path).exists()
                if not item_exists:
                    next_order = FooterMenuItem.objects.filter(menu=menu).count() + 1
                    FooterMenuItem.objects.create(
                        menu=menu,
                        title=self.title,
                        link=link_path,
                        order=next_order
                    )
        except Exception as e:
            print(f"Error auto-adding policy to footer: {e}")

    def delete(self, *args, **kwargs):
        try:
            menu = FooterMenu.objects.filter(title__iexact="Our Policies").first()
            if menu:
                FooterMenuItem.objects.filter(menu=menu, link=f"/{self.slug}").delete()
        except Exception as e:
            print(f"Error removing policy from footer: {e}")
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
