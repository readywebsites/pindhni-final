from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductList, ProductDetail, HeroSlideViewSet, CategoryViewSet, ComfortBeyondTimeSectionDetail,
    BlogViewSet, StoreViewSet, FeatureViewSet, FooterDataView, AnnouncementViewSet,
    SizeViewSet, ColorViewSet, MaterialViewSet, PolicyViewSet
)

router = DefaultRouter()
router.register(r'slides', HeroSlideViewSet, basename='heroslide')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'stores', StoreViewSet, basename='store')
router.register(r'features', FeatureViewSet, basename='feature')
router.register(r'announcements', AnnouncementViewSet, basename='announcement')
router.register(r'sizes', SizeViewSet, basename='size')
router.register(r'colors', ColorViewSet, basename='color')
router.register(r'materials', MaterialViewSet, basename='material')
router.register(r'policies', PolicyViewSet, basename='policy')

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('comfort-beyond-time-section/', ComfortBeyondTimeSectionDetail.as_view(), name='cbt-section'),
    path('footer-data/', FooterDataView.as_view(), name='footer-data'),
    path('', include(router.urls)),
]
