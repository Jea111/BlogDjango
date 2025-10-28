from django.db import models

# Create your models here.

class PanelAdminAdd(models.Model):
    nombre_admin = models.CharField(max_length=200)
    correo_admin = models.CharField(max_length=200)
    password_admin = models.CharField(max_length=200)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'Admin: {self.nombre_admin}'
    
    class Meta:
        verbose_name ='Administrador'
        verbose_name_plural ='Administradores'