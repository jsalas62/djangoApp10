from django.db import models

class Producto(models.Model):
    codigoProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} (ID: {self.codigoProducto})"

class Venta(models.Model):
    codigoVenta = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=100)
    fecha = models.DateTimeField()

    def __str__(self):
        return f"Venta {self.codigoVenta} - Cliente: {self.cliente} - Fecha: {self.fecha.strftime('%Y-%m-%d')}"

class DetalleVenta(models.Model):
    codigoVenta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    codigoProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=18, decimal_places=2)
    descuento = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return f"Detalle Venta {self.id} - Venta: {self.codigoVenta} - Producto: {self.codigoProducto}"
