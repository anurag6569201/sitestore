"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

# Serve React app in production
# Catch-all pattern to serve React app for all non-API routes
if not settings.DEBUG:
    from django.views.static import serve
    import os
    
    def serve_react_app(request):
        """Serve React app - serve Vite's generated index.html"""
        react_dist = os.path.join(settings.BASE_DIR, '..', 'frontend', 'dist')
        index_path = os.path.join(react_dist, 'index.html')
        if os.path.exists(index_path):
            with open(index_path, 'r') as f:
                from django.http import HttpResponse
                return HttpResponse(f.read(), content_type='text/html')
        # Fallback if build doesn't exist
        return TemplateView.as_view(template_name='index.html')(request)
    
    urlpatterns += [
        re_path(r'^(?!admin|api|static|media).*$', serve_react_app),
    ]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

