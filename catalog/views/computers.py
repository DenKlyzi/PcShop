from django.shortcuts import render

def computers(request):
    return render(request, 'catalog/computers/pc_catalog.html')