from django.contrib import admin
from .models import ReseñaBlog,ReseñaTienda

# Register your models here.


@admin.register(ReseñaBlog)
class ReseñaBlogAdmin(admin.ModelAdmin):
    list_display = ('nombre_usuario', 'calificacion', 'blog_comentado', 'created_at')
    search_fields = ('nombre_usuario', 'comentario')
    list_filter = ('calificacion', 'blog_comentado')

@admin.register(ReseñaTienda)
class ReseñaTiendaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'comentario_tienda', 'calificacion_tienda', 'created_at')
    search_fields = ('usuario', 'comentario_tienda')
    list_filter = ('comentario_tienda', 'calificacion_tienda')