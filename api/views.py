from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (
    Product, HeroSlide, Category, ComfortBeyondTimeSection, Blog, Store, Feature,
    FooterSection, FooterMenu, Announcement, Size, Color, Material, Policy, Tag, BlogCategory,
    Subscription
)
from .serializers import (
    ProductSerializer, HeroSlideSerializer, CategorySerializer,
    ComfortBeyondTimeSectionSerializer, BlogSerializer, StoreSerializer, FeatureSerializer,
    FooterSectionSerializer, FooterMenuSerializer, AnnouncementSerializer,
    SizeSerializer, ColorSerializer, MaterialSerializer, PolicySerializer, SubscriptionSerializer
)

def index(request, path=None):
    return render(request, 'index.html')

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        
        # Category Filter
        category_param = self.request.query_params.get('category')
        if category_param:
            category_names = [name.strip().replace('-', ' ').upper() for name in category_param.split(',')]
            queryset = queryset.filter(categories__name__in=category_names).distinct()
            
        # Search Filter
        search_param = self.request.query_params.get('search')
        if search_param:
            queryset = queryset.filter(
                Q(name__icontains=search_param) |
                Q(description__icontains=search_param)
            ).distinct()
            
        return queryset

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class HeroSlideViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing hero slides.
    """
    queryset = HeroSlide.objects.all()
    serializer_class = HeroSlideSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing categories.
    """
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer

class ComfortBeyondTimeSectionDetail(generics.GenericAPIView):
    serializer_class = ComfortBeyondTimeSectionSerializer

    def get(self, request, *args, **kwargs):
        try:
            # For a singleton model, we can just get the latest or first.
            instance = ComfortBeyondTimeSection.objects.latest('id')
        except ComfortBeyondTimeSection.DoesNotExist:
            return Response(status=404)
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing blogs.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        # Get related articles (by tags)
        related_articles = Blog.objects.filter(tags__in=instance.tags.all()).exclude(id=instance.id).distinct()[:3]
        data['related_articles'] = BlogSerializer(related_articles, many=True).data

        # Get previous and next articles
        previous_article = Blog.objects.filter(published_date__lt=instance.published_date).order_by('-published_date').first()
        next_article = Blog.objects.filter(published_date__gt=instance.published_date).order_by('published_date').first()

        if previous_article:
            data['previous_article'] = {'slug': previous_article.slug, 'title': previous_article.title}
        if next_article:
            data['next_article'] = {'slug': next_article.slug, 'title': next_article.title}

        return Response(data)

class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing stores.
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class FeatureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing features.
    """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class FooterDataView(APIView):
    """
    A view to provide all data needed for the footer in a single request.
    """
    def get(self, request, *args, **kwargs):
        try:
            footer_section = FooterSection.objects.latest('id')
        except FooterSection.DoesNotExist:
            footer_section = None
        
        footer_menus = FooterMenu.objects.all()

        data = {
            'section': FooterSectionSerializer(footer_section).data if footer_section else None,
            'menus': FooterMenuSerializer(footer_menus, many=True).data,
        }
        
        return Response(data)

class AnnouncementViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing active announcements.
    """
    queryset = Announcement.objects.filter(active=True)
    serializer_class = AnnouncementSerializer

class SizeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing sizes.
    """
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class ColorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing colors.
    """
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class MaterialViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing materials.
    """
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class PolicyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing policies by slug.
    """
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    lookup_field = 'slug'

class SubscriptionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and creating subscriptions.
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

