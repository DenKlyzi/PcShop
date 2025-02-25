from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'FirstApp/index.html')

def about(request):
    return render(request, 'FirstApp/about.html')

def user(request):
    return render(request, 'FirstApp/user.html')
