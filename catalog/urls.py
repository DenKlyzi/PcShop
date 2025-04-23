from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (
    index, about
)

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
]
