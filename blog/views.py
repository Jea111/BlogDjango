from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogs,FormUser,Ventas,Vendedores

def index(request):
    """muestra todos los blogs en la página principal"""
    all_blogs = Blogs.objects.all()
    return render(request, 'index.html', {'blogs_all': all_blogs})



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
            for item in productos:
                try:
                    blog = Blogs.objects.get(titulo=item['nombre'])
                    Ventas.objects.create(usuario=usuario, producto=blog)
                except Blogs.DoesNotExist:
                    pass 

        return HttpResponse('Pedido creado correctamente')

    return render(request, 'form_user.html')
    
    


def blogSearch(request):
    """ búsqueda de blogs por título """
    query = request.GET.get('q')  # 'q' es el nombre del input
    blogs_search = Blogs.objects.all()

    if query:  # Si el usuario escribió algo
        blogs_search = Blogs.objects.filter(titulo__icontains=query)

    return render(request, 'index.html', {'blogs_inp': blogs_search, 'query': query})


def vendeConNosotros(request):
    """ formulario para que los vendedores agreguen blogs """
    if request.method == 'POST':
        nombre_vendedor = request.POST.get('nombre_vendedor')
        email_vendedor = request.POST.get('email_vendedor')
        telefono_vendedor = request.POST.get('telefono_vendedor')

        titulo = request.POST.get('titulo')
        portada = request.FILES.get('portada')
        autor = request.POST.get('autor')
        precio = request.POST.get('precio')

        vendedor, creado = Vendedores.objects.get_or_create(
            email_vendedor=email_vendedor,
            defaults={
                'nombre_vendedor': nombre_vendedor,
                'telefono_vendedor': telefono_vendedor
            }
        )

        Blogs.objects.create(
            titulo=titulo,
            portada=portada,
            autor=autor,
            precio=precio,
            vendedor=vendedor
        )

        if creado:
            mensaje = "  blog subido exitosamente."
        else:
            mensaje = " Blog creado y vinculado a un vendedor existente."

        return HttpResponse(mensaje)

    return render(request, 'blogs.html')