"""
URL configuration for pindhni project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from api.views import index

# Define URL patterns for different parts of the application
core_urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

static_urlpatterns = []
# Serve static and media files in development
if settings.DEBUG:
    static_urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    static_urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# The SPA catch-all route should be the last pattern
# It serves the index.html file for any route that is not an API, admin, or static file route.
spa_catchall_urlpatterns = [
    re_path(r'^(?!(api/|admin/|ckeditor/|media/|assets/)).*', index, name='index'),
]

# Combine all URL patterns
urlpatterns = core_urlpatterns + static_urlpatterns + spa_catchall_urlpatterns
