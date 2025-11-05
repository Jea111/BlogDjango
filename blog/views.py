from django.shortcuts import render,redirect
from django.http import HttpResponse
from decimal import Decimal, InvalidOperation
from .models import Blogs,FormUser,Ventas,Vendedores
from reseñas.models import ReseñaTienda
from reseñas.views import reseñas_tienda
def index(request):
    """muestra todos los blogs y reseñas en la página principal"""
    all_blogs = Blogs.objects.all()
    reseñas = ReseñaTienda.objects.all().order_by('-created_at')
    return render(request, 'index.html', {
        'blogs_all': all_blogs,
        'reseñas': reseñas
    })



def pedidosUser(request):
    """ formulario para datos del usuario y crear ventas """
    if request.method == 'POST':
        nomb = request.POST.get('nombre')
        direc = request.POST.get('direccion')
        met_p = request.POST.get('metodo_pago')
        carrito = request.POST.get('carrito')

        usuario = FormUser.objects.create(
            nombre=nomb, direccion=direc, metodo_pago=met_p
        )

        # Crear las ventas 
        if carrito:
            import json
            productos = json.loads(carrito)
            # Calcular totales y crear una entrada de venta por cada producto

            for item in productos:
                try:
                    blog = Blogs.objects.get(titulo=item.get('nombre'))
                except Blogs.DoesNotExist:
                    continue

                item_total = None
                if item.get('total') is not None:
                    try:
                        item_total = Decimal(str(item.get('total')))
                    except (InvalidOperation, TypeError):
                        item_total = None

                if item_total is None:
                    try:
                        precio = Decimal(str(item.get('precio', 0)))
                        cantidad = int(item.get('cantidad', 1) or 1)
                        item_total = precio * cantidad
                    except (InvalidOperation, TypeError, ValueError):
                        item_total = Decimal('0.00')

                # Crear la venta asignando el total por producto
                Ventas.objects.create(usuario=usuario, producto=blog, total=item_total)

        return HttpResponse('Pedido creado correctamente')

    return render(request, 'form_user.html')
    
    


# def blogSearch(request):
#     """ búsqueda de blogs por título """
#     query = request.GET.get('q')  # 'q' es el nombre del input
#     blogs_search = Blogs.objects.all()

#     if query:  # Si el usuario escribió algo
#         blogs_search = Blogs.objects.filter(titulo__icontains=query)

#     return render(request, 'index.html', {'blogs_inp': blogs_search, 'query': query})


def vendeConNosotros(request):
    """ formulario para que los vendedores agreguen blogs """
    
    all_blogs = Blogs.objects.all()
    reseñas = ReseñaTienda.objects.all().order_by('-created_at')
    
    
    mensaje = 'Si eres vendedor puedes ingresar al admin con tus credenciales para gestionar las ventas de tus productos aliados'
    
    
    if request.method == 'POST':
        nombre_vendedor = request.POST.get('nombre_vendedor')
        email_vendedor = request.POST.get('email_vendedor')
        telefono_vendedor = request.POST.get('telefono_vendedor')
        password_vendedor = request.POST.get('password_vendedor')

        titulo = request.POST.get('titulo')
        portada = request.FILES.get('portada')
        autor = request.POST.get('autor')
        detalle = request.POST.get('detalle')
        
        precio = request.POST.get('precio')

        vendedor, creado = Vendedores.objects.get_or_create(
            email_vendedor=email_vendedor,
            defaults={
                'nombre_vendedor': nombre_vendedor,
                'telefono_vendedor': telefono_vendedor,
                'password_vendedor':password_vendedor
            }
        )

        Blogs.objects.create(
            titulo=titulo,
            portada=portada,
            autor=autor,
            detalle=detalle,
            precio=precio,
            vendedor=vendedor
        )

        if creado:
            return redirect(index, {
        'blogs_all': all_blogs,
        'reseñas': reseñas
    })

        else:

            return render(request,'index.html',{
        'blogs_all': all_blogs,
        'reseñas': reseñas
    })

    return render(request, 'blogs.html',{'mensaje':mensaje})

def Reseñas(request):
    res = reseñas_tienda()
    
    return render (request,'index.html',res)