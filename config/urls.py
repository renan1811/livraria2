
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaViewSet, EditoraViewSet, AutorViewSet, LivroViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"Editoras", EditoraViewSet)
router.register(r"Autores", AutorViewSet)
router.register(r"Livros", LivroViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]