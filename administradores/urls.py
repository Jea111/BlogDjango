from django.urls import path
from .views import login, Ventas_panel_Admin,eliminar_blog_vendedor,editar_blog_vendedor

urlpatterns = [
    path('login/', login, name='login'),
    path('ventas/', Ventas_panel_Admin, name='ventas'),
    path('panel_vendedores/', login, name='panel_vendedores'),
    path('eliminar_blog/<int:id>/', eliminar_blog_vendedor, name='eliminar_blog'),
    path('editar_blog/<int:id>/', editar_blog_vendedor, name='editar_blog'),

]
