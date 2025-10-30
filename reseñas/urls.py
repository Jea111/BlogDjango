from django.urls import path
from .views import comentarios_blogs

urlpatterns = [
    path('blog_comentado/<int:id>/', comentarios_blogs, name='blog_comentado'),
]
