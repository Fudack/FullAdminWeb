from django import forms
from .models import Productos


#funcion para crear un nuevo producto
class ProductForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario

#funcion para subir archivos excel con datos
class ExcelUploadForm(forms.Form):
    archivo = forms.FileField(label='Selecciona un archivo Excel')



