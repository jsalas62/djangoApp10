from django.contrib import admin
from .models import Producto, Venta, DetalleVenta

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigoProducto', 'nombre', 'precio')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('codigoVenta', 'cliente', 'fecha')

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigoVenta', 'codigoProducto', 'cantidad', 'descuento')
