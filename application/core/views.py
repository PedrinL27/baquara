from django.shortcuts import render, get_object_or_404
from .models import Categoria
from .models import Conteudo

def home(request):
    return render(request, "pages/home.html")

def categorias(request): 

    categorias = Categoria.objects.all()
    
    return render(request, "pages/categorias.html", {
        "categorias": categorias
    })


def manifesto(request):
    return render(request, "pages/manifesto.html")

def sobre(request):
    return render(request, "pages/sobre.html")

def categoria_detail(request, slug):

    categoria = get_object_or_404(Categoria, slug=slug)

    conteudos = Conteudo.objects.filter(
        categorias=categoria,
        status='published'
    )

    return render(request, 'pages/detail/categoria_detail.html', {
        'categoria': categoria,
        'conteudos': conteudos
    })

def conteudo_detail(request, slug):

    conteudo = get_object_or_404(Conteudo, slug=slug)

    return render(request, 'pages/detail/conteudo_detail.html', {
        'conteudo': conteudo
    })