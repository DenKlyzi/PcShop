from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from main.views import index
from authentication.views import login, register

urlpatterns = [
    path('admin', admin.site.urls),
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('catalog/', include('catalog.urls')),
]
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

