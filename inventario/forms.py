from django import forms
from .models import Productos

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario
