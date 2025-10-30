from django.db import models
from blog.models import Blogs

class ReseñaBlog(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    comentario = models.TextField()
    calificacion = models.IntegerField()
    blog_comentado = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='reseñas')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_usuario} - {self.calificacion} estrellas"

    class Meta:
        verbose_name = 'Reseña del blog'
        verbose_name_plural = 'Reseñas de blogs'
