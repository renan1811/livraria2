from rest_framework.serializers import ModelSerializer
from livraria.models.autor import Autor

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"