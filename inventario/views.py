from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Productos




@login_required(login_url='login')
def inventario(request):
    productos = Productos.objects.all()
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario')

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
