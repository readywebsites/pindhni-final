"""
URL configuration for pindhni project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as static_serve
from api.views import index

# Core backend routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# Serve media and specific static directories in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Add a specific rule to serve the /images directory from dist
    urlpatterns.append(re_path(r'^images/(?P<path>.*)$', static_serve, {'document_root': settings.BASE_DIR / 'dist/images'}))

# The SPA catch-all route must be the last pattern.
# It excludes all backend and static/media paths from being handled by the frontend.
urlpatterns.append(re_path(r'^(?!(api/?|admin/?|ckeditor/?|media/?|static/?|images/?)).*$', index, name='index'))
