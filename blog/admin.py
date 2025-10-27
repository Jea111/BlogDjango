from django.contrib import admin
from .models import Blogs,FormUser,Ventas,Vendedores

class BlogItem(admin.ModelAdmin):
    
    fields  = ["titulo",'portada', "autor",'precio',"disponible","vendedor"]
    list_display = ["titulo", "autor",'precio',"disponible","vendedor","fecha"]
    list_filter = ["autor",'precio',"disponible","vendedor"]
    search_fields  = ["titulo","autor",'precio',"disponible","vendedor"]
    
    
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
class ItemVendedores(admin.ModelAdmin):
    fields = ['nombre_vendedor', 'email_vendedor', 'telefono_vendedor']
    list_display = ['nombre_vendedor', 'email_vendedor', 'telefono_vendedor', 'fecha_registro']
    list_filter = ['fecha_registro']
    search_fields = ['nombre_vendedor']
    ordering = ['-fecha_registro']  
    list_per_page = 10 
admin.site.register(Blogs, BlogItem)
admin.site.register(FormUser, formUserItem)
admin.site.register(Ventas, ItemVentas)
admin.site.register(Vendedores, ItemVendedores)
