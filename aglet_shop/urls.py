
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('products/', include('products.urls')),


    ] + static(settings.STATIC_URL, document_too=settings.STATIC_ROOT)
