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
# It serves the index.html file for any URL that doesn't match one of the backend routes above.
# Static files should be handled by the WhiteNoise middleware before this point.
urlpatterns.append(re_path(r'.*', index, name='index'))