from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):

    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    icone = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Tag(models.Model):

    nome = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome


class Conteudo(models.Model):

    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    resumo = models.TextField()
    corpo = models.TextField()

    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    categorias = models.ManyToManyField(Categoria)
    tags = models.ManyToManyField(Tag, blank=True)

    status = models.CharField(max_length=10, choices=STATUS)

    published_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.titulo
    
class Modulo(models.Model):

    conteudo = models.ForeignKey(
        Conteudo,
        on_delete=models.CASCADE,
        related_name='modulos'
    )

    titulo = models.CharField(max_length=200)

    ordem = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo
    
class Aula(models.Model):

    TIPOS = (
        ('video', 'Video'),
        ('pdf', 'PDF'),
        ('texto', 'Texto'),
        ('link', 'Link'),
    )

    modulo = models.ForeignKey(
        Modulo,
        on_delete=models.CASCADE,
        related_name='aulas'
    )

    titulo = models.CharField(max_length=200)

    tipo = models.CharField(max_length=10, choices=TIPOS)

    video_url = models.URLField(blank=True, null=True)

    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)

    conteudo_texto = models.TextField(blank=True)

    ordem = models.IntegerField(default=0)