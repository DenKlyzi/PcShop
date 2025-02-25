from django.urls import path

from FirstApp.apps import FirstappConfig
from FirstApp.views import (
    index, about, user
)

app_name = FirstappConfig.name

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('user/', user, name='user'),
]
