from django.shortcuts import render, get_object_or_404
from .models import Categoria, Conteudo, Aula

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

    return render(request, 'pages/curso/cursos.html', {
        'categoria': categoria,
        'conteudos': conteudos
    })

def conteudo_detail(request, slug):

    conteudo = Conteudo.objects.get(slug=slug)
    modulos = conteudo.modulos.all().order_by('ordem')
    aula_id = request.GET.get("aula")
    aula_atual = None

    if aula_id:
        aula_atual = Aula.objects.get(id=aula_id)

    return render(request, "pages/curso/aulas.html", {
        "conteudo": conteudo,
        "modulos": modulos,
        "aula_atual": aula_atual
    })

# Views para erros personalizados

def erro_404(request, exception):
    return render(request, 'pages/errors/404.html', {
        'path': request.path,
    }, status=404)

def erro_500(request):
    return render(request, 'pages/errors/500.html', status=500)
