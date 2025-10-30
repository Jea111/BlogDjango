from django.contrib import admin
from .models import ReseñaBlog

# Register your models here.


@admin.register(ReseñaBlog)
class ReseñaBlogAdmin(admin.ModelAdmin):
    list_display = ('nombre_usuario', 'calificacion', 'blog_comentado', 'created_at')
    search_fields = ('nombre_usuario', 'comentario')
    list_filter = ('calificacion', 'blog_comentado')

