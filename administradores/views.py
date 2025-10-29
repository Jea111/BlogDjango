from django.shortcuts import render
from blog.models import Ventas, Vendedores, FormUser, Blogs
from .models import PanelAdminAdd


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
                    blog_vendedor = Blogs.objects.filter(vendedor__email_vendedor=correo_admin)
                    ventas_vendedor = Ventas.objects.filter(producto__vendedor__email_vendedor=correo_admin)

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

                context = {
                    'vendedor_blog': blog_vendedor,
                    'ventas_vendedor': ventas_vendedor
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
