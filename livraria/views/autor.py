from rest_framework.viewsets import ModelViewSet

from livraria.serializers.autor import AutorSerializer
from livraria.models.autor import Autor

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
