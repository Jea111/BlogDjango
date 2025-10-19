from django.urls import path
from . views import index,CategoriasInput,pedidosUser,blogSearch


urlpatterns = [
    path('',index,name='index'),
    path('agregarBlogs/',CategoriasInput,name='agregarBlogs'),
    path('pedidos/',pedidosUser,name='pedidos'),
     path('blog_search/', blogSearch, name='blog_search'),
]
