from django.urls import path
from . views import index,CategoriasInput,pedidosUser


urlpatterns = [
    path('',index,name='index'),
    path('agregarBlogs/',CategoriasInput,name='agregarBlogs'),
    path('pedidos/',pedidosUser,name='pedidos')
]
