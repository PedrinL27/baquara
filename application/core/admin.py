from django.contrib import admin
from .models import Categoria, Conteudo, Tag, Modulo, Aula


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = ('nome', 'slug')
    search_fields = ('nome', 'slug')
    prepopulated_fields = {"slug": ("nome",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("nome",)}

class ModuloInline(admin.TabularInline):

    model = Modulo
    extra = 1

@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'published_at')

    list_filter = ('status', 'categorias')

    search_fields = ('titulo',)

    prepopulated_fields = {"slug": ("titulo",)}

    inlines = [ModuloInline]

@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'conteudo', 'ordem')

    list_filter = ('conteudo',)

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'tipo', 'modulo')

    list_filter = ('tipo',)

    search_fields = ('titulo',)
    