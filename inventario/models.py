from django.db import models

#Recursos Humanos
class Empleado(models.Model):
    rut = models.CharField(max_length = 10, unique = True)
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    puesto = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    # Otros campos relacionados con recursos humanos

#Inventario
class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length = 50)
    # Otros campos relacionados con inventario

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)  # Cambio en la longitud para acomodar dígito verificador
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    ciudad = models.CharField(max_length=50)
    # Otros campos relacionados con la gestión de clientes

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero_factura = models.CharField(max_length=20, unique=True)  # Número de factura único
    fecha_emision = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=5, decimal_places=2)  # Porcentaje de IVA aplicado
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Pagada', 'Pagada')])
    # Otros campos relacionados con facturación

class MovimientoContable(models.Model):
    descripcion = models.TextField()
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')])
    # Otros campos relacionados con contabilidad

class CuentaContable(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    # Otros campos relacionados con contabilidad

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Productos, through='DetalleVenta')
    numero_factura = models.CharField(max_length=20, unique=True)  # Número de factura único
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=5, decimal_places=2)  # Porcentaje de IVA aplicado
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Completada', 'Completada')])
    # Otros campos relacionados con ventas

class DetalleVenta(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

class Gasto(models.Model):
    descripcion = models.TextField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    categoria = models.CharField(max_length=50)
    # Otros campos relacionados con finanzas

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, choices=[('En Progreso', 'En Progreso'), ('Completado', 'Completado')])
    # Otros campos relacionados con gestión de proyectos

# Otros modelos para logística, calidad, soporte técnico, etc.




""" opciones_rol = [
    ('usuario', 'Usuario normal'),
    ('admin', 'Administrador')
]

class Cliente(models.Model):
    rut = models.CharField(max_length = 10, unique = True)
    nombre = models.CharField(max_length = 50)
    correo = models.EmailField(unique = True)
    telefono = models.CharField(max_length =12)
    rol = models.CharField(max_length = 7, choices = opciones_rol, default = 'usuario') """

