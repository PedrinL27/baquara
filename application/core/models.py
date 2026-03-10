from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descricao = models.TextField(blank=True)
    descricao_resumida = models.TextField(blank=True)
    icone = models.CharField(max_length=50, blank=True)

    categoria_pai = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='subcategorias'
    )

    def __str__(self):
        return self.nome