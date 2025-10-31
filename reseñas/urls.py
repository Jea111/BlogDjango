from django.urls import path
from .views import comentarios_blogs,reseñas_tienda

urlpatterns = [
    path('blog_comentado/<int:id>/', comentarios_blogs, name='blog_comentado'),
    path('tienda/reseñas/', reseñas_tienda, name='reseñas_tienda'),
]
