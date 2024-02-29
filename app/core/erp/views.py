from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from core.erp.models import Category,Product

def myfirstview(request):
    data = {
        'name'       : 'Camilo',
        'categories' : Category.objects.all()
    }
    #return JsonResponse(data)

    return render(request, 'index.html', data)

def mysecondview(request):
    data = {
        'name'       : 'Camilo',
        'categories' : Category.objects.all(),
        'products'   : Product.objects.all()
    }
    return render(request, 'second.html', data)