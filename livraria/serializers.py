from rest_framework.serializers import ModelSerializer

from livraria.models import Categoria, Editora, Livro, Autor

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"