from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def myfirstview(request):
    data = {
        'name' : 'Camilo'
    }
    #return JsonResponse(data)

    return render(request, 'index.html')
