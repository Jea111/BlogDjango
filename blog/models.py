from django.db import models

# Create your models here.
class Blogs(models.Model):
    titulo = models.CharField(max_length=50)
    portada = models.ImageField(upload_to='media/',null=True, blank=True)
    autor = models.CharField(max_length=150)
    precio = models.DecimalField(decimal_places=2,max_digits=10,null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    disponible= models.BooleanField(default=True)
    
    def __str__(self):
        return f'Autor: {self.autor} - Titulo: {self.titulo} - precio: {self.precio}'
    class Meta:
        verbose_name = 'Blogs'
        verbose_name_plural = 'Blogs'
        
    
    
class FormUser(models.Model):
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    
    def __str__(self):
        return f'Usuario: {self.nombre} - Direcion: {self.direccion} - Metodo pago: {self.metodo_pago}'
    class Meta:
        verbose_name = 'Usuarios'
        verbose_name_plural = 'Usuarios'
        
    
    
class Ventas(models.Model):
    usuario = models.ForeignKey(FormUser,on_delete=models.CASCADE)
    producto = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Usuario Final: {self.usuario.nombre} - Producto: {self.producto.titulo} Fecha Venta: {self.fecha_venta}'
    
    class Meta:
        verbose_name = 'Ventas'
        verbose_name_plural = 'Ventas'
        