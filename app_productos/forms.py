from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'descripcion', 'existencias']
        labels = {
            'nombre': 'Nombre del Producto',
            'categoria': 'Categoría',
            'precio': 'Precio',
            'descripcion': 'Descripción',
            'existencias': 'Existencias',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control', 
                'step': '0.01',
                'min': '0'
            }),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'existencias': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }