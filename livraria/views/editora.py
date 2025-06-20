from rest_framework.viewsets import ModelViewSet
from livraria.models.editora import Editora
from livraria.serializers.editora import EditoraSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer