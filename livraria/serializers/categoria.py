from rest_framework.serializers import ModelSerializer
from livraria.models.categoria import Categoria
class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
