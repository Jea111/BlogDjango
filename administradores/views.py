from django.shortcuts import render
from blog.models import Ventas, Vendedores, FormUser
from .models import PanelAdminAdd


def login(request):
    """Validación de administrador"""
    if request.method == 'POST':
        nombre_admin = request.POST.get('nombre_admin')
        correo_admin = request.POST.get('correo_admin')
        password_admin = request.POST.get('password_admin')

        admin = PanelAdminAdd.objects.filter(correo_admin=correo_admin).first()

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
            else:
                mensaje = 'Contraseña incorrecta'
                return render(request, 'login.html', {'mssg': mensaje})
        else:
            mensaje = 'No tienes acceso como administrador.'
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



