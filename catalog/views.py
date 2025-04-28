from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'catalog/index.html')

def about(request):
    return render(request, 'catalog/about.html')

def user(request):
    return render(request, 'catalog/user.html')
