"""
URL configuration for pindhni project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from api.views import index

# Core backend routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# The SPA catch-all route must be the last pattern.
# It excludes backend-specific paths from being handled by the frontend application.
urlpatterns.append(re_path(r'^(?!(api/|admin/|ckeditor/|media/)).*$', index, name='index'))
