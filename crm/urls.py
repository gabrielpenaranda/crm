from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('apps.core.urls', namespace='core')),
    path('base/', include('apps.base.urls', namespace='base')),
    path('terceros/', include('apps.terceros.urls', namespace='terceros')),
    path('crm/', include('apps.crm.urls', namespace='crm')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)