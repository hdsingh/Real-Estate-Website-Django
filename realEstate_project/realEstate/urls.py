from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('pages.urls')),
    path('admin/', admin.site.urls),
    path('contacts/',include('contacts.urls')),
    path('listing/',include('listings.urls')),
    path('user/',include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
