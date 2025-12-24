from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from blog.models import Ventas, Vendedores, FormUser, Blogs
from .models import PanelAdminAdd
from reseñas.models import ReseñaBlog

def login(request):
    """Validación de administrador y vendedor"""
    if request.method == 'POST':
        nombre_admin = request.POST.get('nombre_admin')
        correo_admin = request.POST.get('correo_admin')
        password_admin = request.POST.get('password_admin')

        # Buscar si es administrador
        admin = PanelAdminAdd.objects.filter(correo_admin=correo_admin).first()

        # Buscar si es vendedor
        vendedor = Vendedores.objects.filter(email_vendedor=correo_admin).first()

        if admin:
            if admin.password_admin == password_admin:
                ventas_admin = Ventas.objects.all()
                vendedores_admin = Vendedores.objects.all()
                formuser_admin = FormUser.objects.all()

                context = {
                    'mssg': f'Bienvenido {admin.nombre_admin}',
                    'ventas_admin': ventas_admin,
                    'vendedores_admin': vendedores_admin,
                    'formuser_admin': formuser_admin,
                }

                return render(request, 'panel.html', context)

            elif vendedor and admin.correo_admin == vendedor.email_vendedor:
                if admin.password_admin == vendedor.password_vendedor:
                    # Obtener los blogs y ventas del vendedor
                    blog = get_object_or_404(Blogs, id=id)
                    
                    blog_vendedor = Blogs.objects.filter(vendedor__email_vendedor=correo_admin)
                    ventas_vendedor = Ventas.objects.filter(producto__vendedor__email_vendedor=correo_admin)
                    reseñas_vendedor = ReseñaBlog.objects.all()
                    

                    #  Inyectar vendedor como usuario 
                    request.user = vendedor
                    request.session['vendedor_id'] = vendedor.id

                    context = {
                        'vendedor_blog': blog_vendedor,
                        'ventas_vendedor': ventas_vendedor,
                        
                    }
                    return render(request, 'panel_vendedores.html', context)
                else:
                    mensaje = 'No tienes acceso como administrador.'
                    return render(request, 'login.html', {'mssg': mensaje})
            else:
                mensaje = 'Contraseña incorrecta.'
                return render(request, 'login.html', {'mssg': mensaje})

        # Si no es administrador, verificar si es vendedor directamente
        elif vendedor:
            if vendedor.password_vendedor == password_admin:
                blog_vendedor = Blogs.objects.filter(vendedor__email_vendedor=correo_admin)
                ventas_vendedor = Ventas.objects.filter(producto__vendedor__email_vendedor=correo_admin)

                #  Inyectar vendedor como usuario 
                request.user = vendedor
                request.session['vendedor_id'] = vendedor.id
                

                context = {
                    'vendedor_blog': blog_vendedor,
                    'ventas_vendedor': ventas_vendedor,
                }
                return render(request, 'panel_vendedores.html', context)
            else:
                mensaje = 'Contraseña incorrecta.'
                return render(request, 'login.html', {'mssg': mensaje})

        else:
            mensaje = 'No tienes acceso al sistema.'
            return render(request, 'login.html', {'mssg': mensaje})

    return render(request, 'login.html', {'mssg': 'Por favor, inicia sesión.'})


def Ventas_panel_Admin(request):
    """Vista para las ventas en plantilla de admin"""
    ventas_admin = Ventas.objects.all()
    vendedores_admin = Vendedores.objects.all()
    formuser_admin = FormUser.objects.all()
    
    

    context = {
        'ventas_admin': ventas_admin,
        'vendedores_admin': vendedores_admin,
        'formuser_admin': formuser_admin,
        
    }

    return render(request, 'panel.html', context)



def eliminar_blog_vendedor(request, id):
    
      #  Recuperar vendedor si se perdió el contexto 
    if not hasattr(request, 'user') or not isinstance(request.user, Vendedores):
        vendedor_id = request.session.get('vendedor_id')
        if vendedor_id:
            request.user = get_object_or_404(Vendedores, id=vendedor_id)
    
    blog_eliminar = get_object_or_404(Blogs, id=id)

    #  verificar que el blog pertenezca al vendedor 
    if blog_eliminar.vendedor != request.user:
        messages.error(request, "No tienes permiso para eliminar este blog.")
        return redirect('panel_vendedores')

    if request.method == 'POST':
        blog_eliminar.delete()
        messages.success(request, 'Blog eliminado exitosamente.')
        return redirect('panel_vendedores')
    
    messages.error(request, 'Acción no válida.')
    return redirect('panel_vendedores')



def editar_blog_vendedor(request, id):

    # Recuperar vendedor desde sesión
    if not hasattr(request, 'user') or not isinstance(request.user, Vendedores):
        vendedor_id = request.session.get('vendedor_id')
        if vendedor_id:
            request.user = get_object_or_404(Vendedores, id=vendedor_id)

    blog_editar = get_object_or_404(Blogs, id=id)

    # Verificar que el blog pertenezca al vendedor
    if blog_editar.vendedor != request.user:
        messages.error(request, "No tienes permiso para editar este blog.")
        return redirect('panel_vendedores')

    if request.method == 'POST':
        # Datos del formulario
        blog_editar.nombre_vendedor = request.POST.get('nombre_vendedor')
        blog_editar.email_vendedor = request.POST.get('email_vendedor')
        blog_editar.telefono_vendedor = request.POST.get('telefono_vendedor')
        blog_editar.password_vendedor = request.POST.get('password_vendedor')
        blog_editar.estado = request.POST.get('estado') == 'true'

        blog_editar.save()
        messages.success(request, 'Vendedor actualizado exitosamente.')
        return render(request,'panel_vendedores.html')

    context = {
        'blog': blog_editar
    }

    return render(request, 'actualizar_blog.html', context)




def eliminar_vendedor_admin(request, id):
    vendedor = get_object_or_404(Vendedores, id=id)
    if vendedor:
        vendedor.delete()
        return redirect('ventas') 
    
    return render(request, 'login.html')

def editar_vendedor(request,id):
    vendedor_editar = get_object_or_404(Vendedores, id=id)
    if request.method =='POST':
        nombre = request.POST.get('nombre_vendedor')
        correo = request.POST.get('email_vendedor')
        telefono = request.POST.get('telefono_vendedor')
        contrasenia = request.POST.get('password_vendedor')
        estatus = True if request.POST.get('estado') == 'true' else False

        
        vendedor_editar.nombre_vendedor =nombre
        vendedor_editar.email_vendedor =correo
        vendedor_editar.telefono_vendedor =telefono
        vendedor_editar.password_vendedor =contrasenia
        vendedor_editar.estado =estatus
        vendedor_editar.save()
        
        messages.success(request, 'vendedor actualizado exitosamente.')
        return redirect('panel_vendedores')
    context = {
        'vende': vendedor_editar
    }
    return render(request, 'actualizar_vendedor.html', context)
    
    
    
def ventasFiltradasView(request):
    """Filtra ventas por nombre del comprador y las muestra en otra plantilla."""

    if request.method == "POST":
        busqueda = request.POST.get("busqueda")
     
        ventas_filtradas = Ventas.objects.filter(usuario__nombre__icontains=busqueda)
        
        return render (request,'panel.html',{'busqueda':busqueda,'ventas_encontradas':ventas_filtradas})
    return redirect('ventas')

