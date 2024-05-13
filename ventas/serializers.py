from rest_framework import serializers
from .models import Producto, Venta, DetalleVenta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

class DetalleVentaSerializer(serializers.ModelSerializer):
    codigoVenta = VentaSerializer(read_only=True)
    codigoProducto = ProductoSerializer(read_only=True)

    codigoVenta_id = serializers.PrimaryKeyRelatedField(
        queryset=Venta.objects.all(),
        source='codigoVenta',
        write_only=True
    )
    codigoProducto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(),
        source='codigoProducto',
        write_only=True
    )

    class Meta:
        model = DetalleVenta
        fields = '__all__'  

