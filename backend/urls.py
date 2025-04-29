from django.contrib import admin
from django.urls import path, include

from main.views import index

from authentication.views.authentication import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('', index, name='index'),
    path('', include('authentication.urls')),
    path('', include('catalog.urls')),
]
