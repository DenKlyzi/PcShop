from django.shortcuts import render
from django.http import HttpResponse

from .models import News

def index(request):
    context = {
        'news': News.objects.all(),
        'title': 'Список новостей'
    }
    return render(request, 'catalog/index.html', context)

def about(request):
    return render(request, 'catalog/about.html')

def user(request):
    return render(request, 'catalog/user.html')
