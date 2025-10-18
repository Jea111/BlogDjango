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
        

        # if porta:
        #     fs = FileSystemStorage()
        #     filename = fs.save(porta.name, porta)
        #     uploaded_file_url = fs.url(filename)
        # else:
        #     uploaded_file_url = None

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
        FormUser.objects.create(nombre=nomb,direccion=direc,metodo_pago=met_p)
        # Ventas.objects.create(usuario=nomb,producto=request.user)
        return HttpResponse('en breve te llegará un mensaje de confirmación')
    
   
    return render(request,'form_user.html')
    
    



