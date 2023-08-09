from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ProductForm
from .models import Productos




@login_required(login_url='login')
def inventario(request):
    form = ProductForm()
    query = request.GET.get('q')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario')

    if query:
        productos = Productos.objects.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(precio_compra__icontains=query) |
            Q(precio_venta__icontains=query) |
            Q(stock__icontains=query) |
            Q(categoria__icontains=query) |
            Q(ubicacion__icontains=query)
        ).distinct()
        
        cant = productos.count()
        if cant == 0:
            productos = Productos.objects.all()
            pass
    else:
        productos = Productos.objects.all()

    context = {'productos': productos, 'form': form}
    return render(request, 'inventario.html', context)




@login_required(login_url='login')
def contabilidad(request):
    return render(request, 'contabilidad.html')


@login_required(login_url='login')
def recursosHumanos(request):
    return render(request, 'recursosHumanos.html')


@login_required(login_url='login')
def facturacion(request):
    return render(request, 'facturacion.html')
