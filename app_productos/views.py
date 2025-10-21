

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})

def ver_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/ver_producto.html', {'producto': producto})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('ver_producto', pk=producto.id)  # Cambia aquí también
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productos/editar_producto.html', {
        'form': form,
        'producto': producto
    })

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'productos/borrar_producto.html', {'producto': producto})