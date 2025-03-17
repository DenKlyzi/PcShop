from django.shortcuts import render
from django.http import HttpResponse

from .models import News

def index(request):
    context = {
        'news': News.objects.all(),
        'title': 'Список новостей'
    }
    return render(request, 'FirstApp/index.html', context)

def about(request):
    return render(request, 'FirstApp/about.html')

def user(request):
    return render(request, 'FirstApp/user.html')
