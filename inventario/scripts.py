from django.shortcuts import render, redirect, HttpResponse


def import_data(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        data_import = pd.read_csv(file)
        for _, row in data_import.iterrows():
            MyModel.objects.create(**row.to_dict())
        return redirect('myapp:index')  # Cambia 'index' por la vista que desees redirigir
    return render(request, 'import_form.html')  # Crea una plantilla para la página de importación
