from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.db.models import Q
from .forms import ProductForm
from .models import Productos
import xlwt


@login_required(login_url='login')
def export_data(request, data):
    print(data)
    response = HttpResponse(content_type='aplication/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data_export.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Data')
    row_num = 0
    for row in data:
        for col_num, value in numerate(row.values()):
            ws.write(row_num, col_num, value)
        row_num += 1
    
    wb.save(response)
    return response


@login_required(login_url='login')
def inventario(request):
    form = ProductForm()
    query = request.GET.get('q')
    
    data = list(Productos.objects.all().values())
    
    if request.GET.get('export'):
        return export_data(request, data)
    
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
