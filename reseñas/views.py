from django.shortcuts import render, get_object_or_404
from blog.models import Blogs,FormUser
from .models import ReseñaBlog,ReseñaTienda

def comentarios_blogs(request, id):
    blog = get_object_or_404(Blogs, id=id)

    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombreUsuario')
        comentario = request.POST.get('comentario')
        calificacion = request.POST.get('calificacion')

        if not nombre_usuario:
            reseñas = ReseñaBlog.objects.filter(blog_comentado=blog)
            mensaje = 'El campo "Tu nombre" es obligatorio para dejar una reseña del blog.'
            return render(request, 'blog_reseñas.html', {'blog': blog, 'reseñas': reseñas, 'mensaje': mensaje})

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


def reseñas_tienda(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('usuario') or request.POST.get('nombreUsuario_tienda')
        comentario = request.POST.get('comentario_tienda')
        calificacion = request.POST.get('calificacion_tienda')
        usuario = FormUser.objects.filter(nombre=nombre_usuario).first()

       
        if not usuario and nombre_usuario:
            usuario = FormUser.objects.create(
                nombre=nombre_usuario,
                direccion='medellin',
                metodo_pago='efectivo'
            )

        if not usuario:
            reseñas = ReseñaTienda.objects.all().order_by('-created_at')
            mensaje = 'Debe indicar su nombre para dejar una reseña de la tienda.'
            return render(request, 'index.html', {'mensaje': mensaje, 'reseñas': reseñas})

        try:
            cal = int(calificacion) if calificacion else None
        except (ValueError, TypeError):
            cal = None

        ReseñaTienda.objects.create(
            usuario=usuario,
            comentario_tienda=comentario,
            calificacion_tienda=cal
        )

        reseñas = ReseñaTienda.objects.all().order_by('-created_at')
        mensaje = 'Reseña de la tienda creada correctamente.'
        return render(request, 'index.html', {'mensaje': mensaje, 'reseñas': reseñas})
    reseñas = ReseñaTienda.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'reseñas': reseñas})