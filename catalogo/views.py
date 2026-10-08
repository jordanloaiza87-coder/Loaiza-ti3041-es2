from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito, ItemCarrito
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django import forms

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo/index.html', {'productos': productos})

@login_required
def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    # Obtener la cantidad del formulario (por defecto 1)
    cantidad = int(request.POST.get('cantidad', 1))

    if producto.stock >= cantidad:
        carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
        item, item_creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
        
        if not item_creado:
            item.cantidad += cantidad
            item.save()
        else:
            item.cantidad = cantidad
            item.save()
            
    return redirect('inicio')

@login_required
def ver_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    items = ItemCarrito.objects.filter(carrito=carrito)

    if request.method == 'POST':  # Al presionar "Confirmar Compra"
        for item in items:
            if item.producto.stock >= item.cantidad:
                item.producto.stock -= item.cantidad
                item.producto.save()  # Descuenta el stock de la base de datos
        items.delete()  # Vacía el carrito
        return redirect('inicio')

    return render(request, 'catalogo/carrito.html', {'items': items})

@user_passes_test(lambda u: u.is_superuser)
def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio') # Vuelve al catálogo tras crearlo
    else:
        form = UserCreationForm()
    
    return render(request, 'catalogo/registrar_usuario.html', {'form': form})

# Vista para AGREGAR un nuevo producto
@user_passes_test(lambda u: u.is_superuser)
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProductoForm()
        
    return render(request, 'catalogo/agregar_producto.html', {'form': form})

# Vista para ELIMINAR un producto
@user_passes_test(lambda u: u.is_superuser)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('inicio')
        
    return render(request, 'catalogo/eliminar_producto.html', {'producto': producto})

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'stock', 'imagen', 'imagen_url']

@user_passes_test(lambda u: u.is_superuser)
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProductoForm(instance=producto)
        
    return render(request, 'catalogo/editar_producto.html', {'form': form, 'producto': producto})