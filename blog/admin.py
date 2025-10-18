from django.contrib import admin
from .models import Blogs,FormUser,Ventas

class BlogItem(admin.ModelAdmin):
    
    fields  = ["titulo", "autor",'precio',"disponible"]
    list_display = ["titulo", "autor",'precio',"disponible"]
    list_filter = ["autor",'precio',"disponible"]
    search_fields  = ["titulo", "autor",'precio',"disponible"]
    
    
class formUserItem(admin.ModelAdmin):
    fields = ['nombre','direccion','metodo_pago']
    list_display = ['nombre','direccion','metodo_pago']
    list_filter = ['nombre','direccion','metodo_pago']
    search_fields = ['nombre','direccion','metodo_pago']
    
    
class ItemVentas(admin.ModelAdmin):
    fields = ['usuario','producto']
    list_display = ['usuario','producto','fecha_venta']
    list_filter = ['usuario','producto','fecha_venta']
    search_fields = ['usuario','producto','fecha_venta']

admin.site.register(Blogs, BlogItem)
admin.site.register(FormUser, formUserItem)
admin.site.register(Ventas, ItemVentas)
