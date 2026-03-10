from django.shortcuts import render
from .models import Categoria

def home(request):
    return render(request, "pages/home.html")

def categorias(request): 
    categorias = Categoria.objects.filter(categoria_pai=None)

    return render(request, "pages/categorias.html", {
        "categorias": categorias
    })


def manifesto(request):
    return render(request, "pages/manifesto.html")

def sobre(request):
    return render(request, "pages/sobre.html")