from rest_framework.serializers import ModelSerializer
from livraria.models.autor import Autor
from uploader.serializers import ImageSerializer
class AutorSerializer(ModelSerializer):

    foto = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Autor
        fields = "__all__"