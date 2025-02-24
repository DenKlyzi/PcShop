from django.urls import path
from FirstApp import views
from FirstApp.apps import FirstappConfig

app_name = FirstappConfig.name

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user/', views.user, name='user'),
]
