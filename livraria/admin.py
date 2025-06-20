from django.contrib import admin

# Register your models here.
from .models import Categoria, Autor, Livro, Editora, Compra,ItensCompra

@admin.register(ItensCompra)
class ItensCompraAdmin(admin.ModelAdmin):
    list_display = ['id', 'compra', 'livro', 'quantidade']
    search_fields = ['livro__titulo', 'compra__id']
    list_filter = ['compra']

class ItensCompraInline(admin.TabularInline):
    model = ItensCompra
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]
    list_display = ("usuario", "status")
    ordering = ("-id",)
    list_per_page = 25
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email', 'foto')
    list_filter = ('nome',)
    ordering = ('nome', 'email')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'editora', 'categoria')
    search_fields = ('nome', 'editora__nome', 'categoria__descricao')
    list_filter = ('editora', 'categoria')
    ordering = ('nome', 'editora', 'categoria')
    list_per_page = 25