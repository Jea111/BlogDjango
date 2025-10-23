from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Blogs,FormUser,Ventas

def index(request):
    all_blogs = Blogs.objects.all()
    return render(request, 'index.html', {'blogs_all': all_blogs})


def CategoriasInput(request):
    if request.method == 'POST':
        titu = request.POST.get('titulo')         
        aut = request.POST.get('autor')                  
        porta = request.FILES.get('portada')      
        preci = request.POST.get('precio')       

        Blogs.objects.create(
            titulo=titu,
            portada=porta,  
            autor=aut,
            precio=preci
        )

        return redirect('index') 
    
    return render(request, 'blogs.html')


def pedidosUser(request):
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
    query = request.GET.get('q')  # 'q' es el nombre del input
    blogs_search = Blogs.objects.all()

    if query:  # Si el usuario escribió algo
        blogs_search = Blogs.objects.filter(titulo__icontains=query)

    return render(request, 'index.html', {'blogs_inp': blogs_search, 'query': query})