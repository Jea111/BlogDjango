from django.shortcuts import render, get_object_or_404
from blog.models import Blogs
from .models import ReseñaBlog

def comentarios_blogs(request, id):
    blog = get_object_or_404(Blogs, id=id)

    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombreUsuario')
        comentario = request.POST.get('comentario')
        calificacion = request.POST.get('calificacion')

        # Crear la reseña
        ReseñaBlog.objects.create(
            nombre_usuario=nombre_usuario,
            comentario=comentario,
            calificacion=calificacion,
            blog_comentado=blog
        )

        mensaje = f"Comentario creado exitosamente por {nombre_usuario}"
        return render(request, 'blog_reseñas.html', {'mensaje': mensaje, 'blog': blog})

    reseñas = ReseñaBlog.objects.filter(blog_comentado=blog)
    return render(request, 'blog_reseñas.html', {'blog': blog, 'reseñas': reseñas})
