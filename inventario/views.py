from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def invetario(request):
    return render(request, 'inventario.html')

@login_required(login_url='login')
def contabilidad(request):
    return render(request, 'contabilidad.html')


@login_required(login_url='login')
def recursosHumanos(request):
    return render(request, 'recursosHumanos.html')


@login_required(login_url='login')
def facturacion(request):
    return render(request, 'facturacion.html')
