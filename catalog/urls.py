from django.conf.urls.static import static
from django.conf import settings
from django.urls import path


from catalog.views import *

urlpatterns = [
    path('computers/', computers, name='computers'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
