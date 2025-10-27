from django.urls import path
from . views import index,pedidosUser,blogSearch,vendeConNosotros


urlpatterns = [
    path('',index,name='index'),
    path('agregarBlogs/',vendeConNosotros,name='agregarBlogs'),
    path('pedidos/',pedidosUser,name='pedidos'),
    path('blog_search/', blogSearch, name='blog_search'),
     
]
