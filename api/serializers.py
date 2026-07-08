from rest_framework import serializers
from .models import (
    Product, HeroSlide, Category, ComfortBeyondTimeSection, Blog, Store, Feature,
    FooterSection, SocialLink, FooterMenu, FooterMenuItem, Announcement,
    Size, Color, Material, ProductSize, Policy, Tag, BlogCategory, Subscription
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'is_active', 'show_on_navbar']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']

class ProductSizeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='size.id')
    name = serializers.ReadOnlyField(source='size.name')

    class Meta:
        model = ProductSize
        fields = ['id', 'name', 'in_stock']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'hex']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Category.objects.all(), source='categories'
    )
    sizes = ProductSizeSerializer(many=True, read_only=True, source='product_sizes')
    size_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Size.objects.all(), source='sizes', required=False
    )
    colors = ColorSerializer(many=True, read_only=True)
    color_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Color.objects.all(), source='colors', required=False
    )
    materials = MaterialSerializer(many=True, read_only=True)
    material_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Material.objects.all(), source='materials', required=False
    )
    price = serializers.SerializerMethodField()
    original_price = serializers.SerializerMethodField()
    discount_percentage = serializers.SerializerMethodField()

    def get_price(self, obj):
        price = float(obj.price)
        if obj.discount_type == 'percent' and obj.discount_value > 0:
            return round(price * (1 - float(obj.discount_value) / 100), 2)
        elif obj.discount_type == 'amount' and obj.discount_value > 0:
            return max(round(price - float(obj.discount_value), 2), 0.0)
        return price

    def get_original_price(self, obj):
        if obj.discount_type != 'none' and obj.discount_value > 0:
            return float(obj.price)
        return None

    def get_discount_percentage(self, obj):
        if obj.discount_type == 'percent' and obj.discount_value > 0:
            return int(obj.discount_value)
        elif obj.discount_type == 'amount' and obj.discount_value > 0 and obj.price > 0:
            return int(round((float(obj.discount_value) / float(obj.price)) * 100))
        return None

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'original_price', 'discount_percentage',
            'discount_type', 'discount_value', 'image', 'in_stock',
            'is_new_arrival', 'is_bestseller', 'is_featured',
            'detail_image_1', 'detail_image_2', 'detail_image_3',
            'detail_image_4', 'detail_image_5', 'detail_image_6',
            'detail_image_7', 'detail_image_8', 'detail_image_9',
            'details', 'material_care', 'shipping',
            'categories', 'category_ids',
            'sizes', 'size_ids',
            'colors', 'color_ids',
            'materials', 'material_ids'
        ]

class HeroSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSlide
        fields = '__all__'

class ComfortBeyondTimeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComfortBeyondTimeSection
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['name']

class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Blog
        fields = '__all__'
        lookup_field = 'slug'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

# Footer Serializers
class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['icon', 'link']

class FooterMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterMenuItem
        fields = ['title', 'link']

class FooterMenuSerializer(serializers.ModelSerializer):
    items = FooterMenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = FooterMenu
        fields = ['title', 'items']

class FooterSectionSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True, read_only=True)

    class Meta:
        model = FooterSection
        fields = ['newsletter_text', 'copyright_line_1', 'copyright_line_2', 'social_links']

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'text']

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ['id', 'title', 'policy', 'slug']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

