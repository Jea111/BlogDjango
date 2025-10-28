from django.db import models

class Vendedores(models.Model):
    nombre_vendedor = models.CharField(max_length=120)
    email_vendedor = models.EmailField(max_length=254, unique=True)
    telefono_vendedor = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Vendedor: {self.nombre_vendedor} '

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'


class Blogs(models.Model):
    titulo = models.CharField(max_length=50)
    portada = models.ImageField(upload_to='media/', null=True, blank=True)
    autor = models.CharField(max_length=150)
    precio = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    disponible = models.BooleanField(default=True)
    vendedor = models.ForeignKey(Vendedores, on_delete=models.SET_NULL, related_name='blogs', null=True, blank=True)

    def __str__(self):
        return f'Autor: {self.autor} - Título: {self.titulo} - Precio: {self.precio}'

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class FormUser(models.Model):
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f'Usuario: {self.nombre} - Dirección: {self.direccion} - Método pago: {self.metodo_pago}'

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Ventas(models.Model):
    usuario = models.ForeignKey(FormUser, on_delete=models.CASCADE)
    producto = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=2, max_digits=10,null=True, blank=True,default=5.00)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Usuario: {self.usuario.nombre} - Producto: {self.producto.titulo} '

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
