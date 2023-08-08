from django.shortcuts import render


def invetario(request):
    return render(request, 'inventario.html')

def contabilidad(request):
    return render(request, 'inventario.html')
# Create your views here.
