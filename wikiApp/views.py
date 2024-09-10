from django.shortcuts import render, get_object_or_404, redirect
from .models import temaWiki, articuloWiki

def index(request):
    listaTemas = temaWiki.objects.all().order_by('id')
    
    return render(request, 'wikiApp/index.html',{'listaTemas':listaTemas})
# return render(request, 'wikiApp/index.html', {'temas': temas})

def crear_tema(request):
    listaTemas = temaWiki.objects.all().order_by('id')
    if request.method == 'POST':
        # Lógica para manejar la creación de un nuevo tema
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        objTema = temaWiki.objects.create(nombre = nombre,descripcion = descripcion)
        objTema.save()

    return render(request, 'wikiApp/crear_tema.html',{'listaTemas':listaTemas})

def crear_articulo(request):
    listaTemas = temaWiki.objects.all().order_by('id')
    listaArticulos = articuloWiki.objects.all().order_by('id') 

    if request.method == 'POST':
        # Lógica para manejar la creación de un nuevo tema
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        temaRelacionado_id = request.POST.get('temaRelacionado')

        try:
            temaRelacionado = temaWiki.objects.get(id=temaRelacionado_id)
            objArticulo = articuloWiki.objects.create(
                titulo=titulo,
                contenido=contenido,
                temaRelacionado=temaRelacionado
            )

       
            objArticulo.save()       
            return redirect('index')
    
        except temaWiki.DoesNotExist:
            return render(request, 'wikiApp/crear_articulo.html', {
                'listaTemas': listaTemas,
                'error_message': 'El tema seleccionado no existe.'
            })
    
    return render(request, 'wikiApp/crear_articulo.html',{'listaTemas':listaTemas})

# def articulos_por_tema(request, tema_id):
#     tema = get_object_or_404(temaWiki, id=tema_id)
#     articulos = articuloWiki.objects.filter(tema=tema)
#     return render(request, 'wikiApp/articulos_por_tema.html', {'tema': tema, 'articulos': articulos})
