from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from decouple import config

urlpatterns = [
    path(config('ADMIN_URL'), admin.site.urls),
    path('loja/', include('store.urls')),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
