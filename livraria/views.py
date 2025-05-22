
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from livraria.models import Categoria, Autor, Livro, editora
from livraria.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer, LivroSerializer, LivroDetailSerializer, LivroListSerializer



