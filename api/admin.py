from django.contrib import admin
from django import forms
from django.utils.html import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import (
    Product, Category, HeroSlide, ComfortBeyondTimeSection, Blog, Store, Feature,
    FooterSection, SocialLink, FooterMenu, FooterMenuItem, Announcement,
    Size, Color, Material, ProductSize, Policy
)

# Forms with CKEditor
class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    details = forms.CharField(widget=CKEditorUploadingWidget(), required=False)
    material_care = forms.CharField(widget=CKEditorUploadingWidget(), required=False)
    shipping = forms.CharField(widget=CKEditorUploadingWidget(), required=False)
    class Meta:
        model = Product
        fields = '__all__'

class ComfortBeyondTimeSectionAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = ComfortBeyondTimeSection
        fields = '__all__'

class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Blog
        fields = '__all__'

class FeatureAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Feature
        fields = '__all__'

class FooterSectionAdminForm(forms.ModelForm):
    newsletter_text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = FooterSection
        fields = '__all__'

class PolicyAdminForm(forms.ModelForm):
    policy = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Policy
        fields = '__all__'

# ModelAdmins
class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('name', 'price', 'discount_type', 'discount_value', 'in_stock', 'is_new_arrival', 'is_bestseller', 'is_featured', 'image_thumbnail')
    list_editable = ('discount_type', 'discount_value', 'in_stock', 'is_new_arrival', 'is_bestseller', 'is_featured')
    readonly_fields = ('image_thumbnail',)
    filter_horizontal = ('colors', 'categories', 'materials')
    inlines = [ProductSizeInline]

    def image_thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}" width="100" /></a>')
        return "No Image"
    image_thumbnail.short_description = 'Image'

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('order', 'button_text', 'image_thumbnail', 'mobile_image_thumbnail')
    readonly_fields = ('image_thumbnail', 'mobile_image_thumbnail')

    def image_thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}" width="150" /></a>')
        return "No Image"
    image_thumbnail.short_description = 'Desktop Image'

    def mobile_image_thumbnail(self, obj):
        if obj.mobile_image:
            return mark_safe(f'<a href="{obj.mobile_image.url}" target="_blank"><img src="{obj.mobile_image.url}" width="100" /></a>')
        return "No Mobile Image"
    mobile_image_thumbnail.short_description = 'Mobile Image'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass

@admin.register(ComfortBeyondTimeSection)
class ComfortBeyondTimeSectionAdmin(admin.ModelAdmin):
    form = ComfortBeyondTimeSectionAdminForm
    list_display = ('title', 'subtitle', 'image1_thumbnail', 'image2_thumbnail')
    readonly_fields = ('image1_thumbnail', 'image2_thumbnail')

    def image1_thumbnail(self, obj):
        if obj.image1:
            return mark_safe(f'<a href="{obj.image1.url}" target="_blank"><img src="{obj.image1.url}" width="100" /></a>')
        return "No Image"
    image1_thumbnail.short_description = 'Image 1 (Vertical)'

    def image2_thumbnail(self, obj):
        if obj.image2:
            return mark_safe(f'<a href="{obj.image2.url}" target="_blank"><img src="{obj.image2.url}" width="150" /></a>')
        return "No Image"
    image2_thumbnail.short_description = 'Image 2 (Horizontal)'

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ('title', 'published_date', 'image_thumbnail')
    readonly_fields = ('image_thumbnail',)
    prepopulated_fields = {'slug': ('title',)}

    def image_thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}" width="100" /></a>')
        return "No Image"
    image_thumbnail.short_description = 'Image'

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('title', 'address')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    form = FeatureAdminForm
    list_display = ('title', 'icon', 'order')
    list_editable = ('order',)

# Footer Admin
class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1

@admin.register(FooterSection)
class FooterSectionAdmin(admin.ModelAdmin):
    form = FooterSectionAdminForm
    inlines = [SocialLinkInline]

class FooterMenuItemInline(admin.TabularInline):
    model = FooterMenuItem
    extra = 1

@admin.register(FooterMenu)
class FooterMenuAdmin(admin.ModelAdmin):
    inlines = [FooterMenuItemInline]
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('text', 'active', 'order')
    list_editable = ('active', 'order')

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    form = PolicyAdminForm
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
