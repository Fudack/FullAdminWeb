from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import ProductForm, ExcelUploadForm
from .models import Productos
from openpyxl.styles import NamedStyle, Font
from openpyxl import Workbook
from django.shortcuts import render, redirect


@login_required(login_url='login')
def import_data(request):
    print('import_data')
    excel_form = ExcelUploadForm()  # Crea una instancia del formulario ExcelUploadForm

    if request.method == 'POST':
        excel_form = ExcelUploadForm(request.POST, request.FILES)
        if excel_form.is_valid():
            excel_file = request.FILES['archivo']
            wb = openpyxl.load_workbook(excel_file)
            worksheet = wb.active
            for row in worksheet.iter_rows():
                nombre = row[0].value
                descripcion = row[1].value
                precio_compra = row[2].value
                precio_venta = row[3].value
                stock = row[4].value
                categoria = row[5].value
                ubicacion = row[6].value
                Productos.objects.create(
                    nombre=nombre,
                    descripcion=descripcion,
                    precio_compra=precio_compra,
                    precio_venta=precio_venta,
                    stock=stock,
                    categoria=categoria,
                    ubicacion=ubicacion
                )
            return redirect('product_list')  # Redirige a la lista de productos

    context = {'excel_form': excel_form}
    return render(request, 'inventario.html', context)  # Renderiza la misma página con el formulario


@login_required(login_url='login')
def export_data(request, data, data_titles, name):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename={}.xlsx'.format(name)
    
    wb = Workbook()
    ws = wb.active

    header_style = NamedStyle(name="header_style")
    header_style.font = Font(bold=True)
    wb.add_named_style(header_style)

    headers = [field for field in data_titles]

    for col_num, header in enumerate(headers[2:], start=1):
        cell = ws.cell(row=1, column=col_num, value=header)
        cell.style = "header_style"

    data_style = NamedStyle(name="data_style")
    data_style.alignment.horizontal = "left"
    wb.add_named_style(data_style)

    for row_num, row in enumerate(data, start=2):
        for col_num, value in enumerate(row, start=1):
            cell = ws.cell(row=row_num, column=col_num, value=value)
            cell.style = "data_style"

    wb.save(response)
    return response

@login_required(login_url='login')
def product_list(request):
    form = ProductForm()
    import_form = ExcelUploadForm()
    productos = Productos.objects.all()
    unique_categories = productos.values_list('categoria', flat=True).distinct()
    unique_ubicacion = productos.values_list('ubicacion', flat=True).distinct()
    data_titles = [field.name for field in Productos._meta.get_fields()]

    if request.GET.get('exportar'):
        data = [list(row.values()) for row in productos.values()]
        name = 'inventario'
        return export_data(request, data, data_titles, name)

    elif request.GET.get('formato'):
        data = []
        name = 'formato'
        return export_data(request, data, data_titles, name)

    elif request.method == 'POST' and 'import_file' in request.FILES:
        return import_data(request)


    elif 'c' in request.GET:
        filter_categories = request.GET.get('c')
        productos = Productos.objects.filter(
            Q(categoria__icontains=filter_categories)
        ).distinct()

    elif 'u' in request.GET:
        filter_ubication = request.GET.get('u')
        productos = Productos.objects.filter(
            Q(ubicacion__icontains=filter_ubication)
        ).distinct()

    elif 'q' in request.GET:
        query = request.GET.get('q')
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

    elif request.method == 'POST':
        form_add = ProductForm(request.POST)
        
        if form_add.is_valid():
            form_add.save()
            return redirect('product_list')
        
        elif 'import_file' in request.FILES:
            excel_form = ExcelUploadForm(request.POST, request.FILES)
        if excel_form.is_valid():
            excel_file = request.FILES['archivo']
            wb = openpyxl.load_workbook(excel_file)
            worksheet = wb.active
            for row in worksheet.iter_rows():
                nombre = row[0].value
                descripcion = row[1].value
                precio_compra = row[2].value
                precio_venta = row[3].value
                stock = row[4].value
                categoria = row[5].value
                ubicacion = row[6].value
                Productos.objects.create(
                    nombre=nombre,
                    descripcion=descripcion,
                    precio_compra=precio_compra,
                    precio_venta=precio_venta,
                    stock=stock,
                    categoria=categoria,
                    ubicacion=ubicacion
                )
            return redirect('product_list')

    context = {
        'productos': productos,
        'form': form,
        'import_form': import_form,
        'unique_categories': unique_categories,
        'unique_ubicacion': unique_ubicacion
    }
    return render(request, 'inventario.html', context)

# Resto de las vistas sin cambios

@login_required(login_url='login')
def contabilidad(request):
    return render(request, 'contabilidad.html')

@login_required(login_url='login')
def recursosHumanos(request):
    return render(request, 'recursosHumanos.html')

@login_required(login_url='login')
def facturacion(request):
    return render(request, 'facturacion.html')
