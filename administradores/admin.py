from django.contrib import admin
from . models import PanelAdminAdd
# Register your models here.

class adminItem(admin.ModelAdmin):
    fields = ['nombre_admin','correo_admin','password_admin']
    list_display= ['nombre_admin','correo_admin']
    list_filter= ['nombre_admin','correo_admin']
    search_fields= ['nombre_admin','correo_admin']
    
admin.site.register(PanelAdminAdd,adminItem)

